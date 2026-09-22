#!/usr/bin/env python3
"""SYNTHETIC TEST FIXTURE - NOT INDEPENDENT BENCHMARK EVIDENCE.

Plan or apply a staged deployment. --plan is read-only and the default.
"""
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Plan or apply a deployment.")
    parser.add_argument("--plan", action="store_true", default=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    env = os.environ.get("DEPLOY_ENV")
    if not env:
        raise SystemExit("DEPLOY_ENV is unset")
    print(f"{'apply' if args.apply else 'plan'} against {env}")


if __name__ == "__main__":
    main()
