import os
from datetime import datetime
import textwrap

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm


class PdfReport:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _wrap(self, text, width_chars=90):
        return textwrap.wrap(text, width=width_chars)

    def build(self, run_id, title, executive_summary, hypotheses, creatives, actions):
        filename = os.path.join(self.output_dir, f"dashboard_{run_id}.pdf")
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        margin = 20 * mm

        y = height - margin
        x = margin

        c.setFont("Helvetica-Bold", 16)
        c.drawString(x, y, title)
        c.setFont("Helvetica", 8)
        c.drawRightString(width - margin, y, f"Run: {run_id} | Generated: {datetime.utcnow().isoformat()}")
        y -= 20

        # Executive summary
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, "Executive Summary")
        y -= 14
        c.setFont("Helvetica", 9)
        for line in self._wrap(executive_summary, 110):
            c.drawString(x, y, line)
            y -= 11

        y -= 10
        # Hypotheses
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, "Top Hypotheses")
        y -= 14
        c.setFont("Helvetica", 9)
        for h in hypotheses[:4]:
            text = f"{h['id']} [{h['confidence']:.2f}] - {h['text']}"
            for line in self._wrap(text, 110):
                c.drawString(x + 10, y, line)
                y -= 11
            y -= 4

        # Creatives on right side
        rx = width / 2
        ry = height / 2
        c.setFont("Helvetica-Bold", 12)
        c.drawString(rx, ry, "Top Simulated Creatives")
        ry -= 14
        c.setFont("Helvetica", 9)
        for cr in creatives[:6]:
            text = f"{cr.get('campaign_name','?')} | CTR~{cr['predicted_ctr']:.3f} | {cr['message'][:80]}"
            for line in self._wrap(text, 60):
                c.drawString(rx, ry, line)
                ry -= 11
            ry -= 4

        # Actions
        ay = margin + 50
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, ay, "Recommended Actions")
        ay -= 14
        c.setFont("Helvetica", 9)
        for i, a in enumerate(actions[:5], start=1):
            for line in self._wrap(f"{i}. {a}", 110):
                c.drawString(x + 10, ay, line)
                ay -= 11

        c.save()
        return filename
