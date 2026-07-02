# agent-state-check

> Audit agent state schemas for persistence, reset, and user isolation risks.

## Operator guide Overview

Audit agent state schemas for persistence, reset, and user isolation risks. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts agent state schema. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
agent-state-check examples/sample.txt
agent-state-check examples/sample.txt --json --fail-on medium
python -m agent_state_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `persistent-state` | high | persistent state detected |
| `missing-reset` | medium | reset behavior missing |
| `missing-isolation` | low | user isolation unclear |

## Validation Notes

```bash
ruff check .
pytest
python -m agent_state_check --help
```

Example risky input:

```text
state persistent reset none user_isolation missing
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
