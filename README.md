<p align="center">
  <img src="assets/readme-cover.svg" alt="Agent State Check cover" width="100%" />
</p>

# Agent State Check

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Audit agent state schemas for persistence, reset, and user isolation risks.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `agent-state-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
agent-state-check examples/sample.txt
agent-state-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `persistent-state` | high | persistent state detected |
| `missing-reset` | medium | reset behavior missing |
| `missing-isolation` | low | user isolation unclear |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
state persistent reset none user_isolation missing
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m agent_state_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Agent State Check policy easy to review.
