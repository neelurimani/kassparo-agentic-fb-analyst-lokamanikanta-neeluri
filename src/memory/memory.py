import json
import os
from datetime import datetime
from typing import Any, Dict, List


class Memory:
    def __init__(self, path: str = "memory/memory.json", max_events: int = 500):
        self.path = path
        self.max_events = max_events
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            self._init_store()
        self._load()

    def _init_store(self):
        with open(self.path, "w") as f:
            json.dump(
                {"meta": {"created": datetime.utcnow().isoformat()}, "store": {}, "events": []},
                f,
                indent=2,
            )

    def _load(self):
        with open(self.path, "r") as f:
            self._data = json.load(f)

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)

    def remember(self, key: str, value: Any):
        self._data["store"][key] = {"value": value, "ts": datetime.utcnow().isoformat()}
        self._save()

    def recall(self, key: str, default=None):
        return self._data["store"].get(key, {}).get("value", default)

    def append_event(self, event: Dict):
        event = dict(event)
        event["ts"] = datetime.utcnow().isoformat()
        self._data["events"].append(event)
        if len(self._data["events"]) > self.max_events:
            self._data["events"] = self._data["events"][-self.max_events :]
        self._save()

    def list_events(self, limit: int = 50) -> List[Dict]:
        return self._data["events"][-limit:]
