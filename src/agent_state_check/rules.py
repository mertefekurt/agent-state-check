from __future__ import annotations

from agent_state_check.models import Rule

PROJECT_NAME = 'agent-state-check'
SUMMARY = 'Audit agent state schemas for persistence, reset, and user isolation risks.'
SAMPLE_RISK = 'state persistent reset none user_isolation missing'
SAMPLE_CLEAN = 'state session reset supported user_isolation tenant'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='persistent-state',
        severity='high',
        pattern='state\\s+persistent',
        message='persistent state detected',
        recommendation='review retention and deletion',
    ),
    Rule(
        code='missing-reset',
        severity='medium',
        pattern='reset\\s+(none|missing|unknown)',
        message='reset behavior missing',
        recommendation='add state reset path',
    ),
    Rule(
        code='missing-isolation',
        severity='low',
        pattern='user_isolation\\s+(missing|none|unknown)',
        message='user isolation unclear',
        recommendation='scope state by user or tenant',
    ),
)
