#!/usr/bin/env python3
import argparse
import yaml
from src.orchestrator import Orchestrator


def main():
    print(">>> run.py started")

    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str)
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    print(f"> Query received: {args.query}")

    cfg = yaml.safe_load(open(args.config, "r"))
    print("> Loaded config")

    orch = Orchestrator(cfg)
    print("> Orchestrator initialized")

    result = orch.run(args.query)
    print("> Pipeline finished")

    print(result)


if __name__ == "__main__":
    main()
