"""Enumeration of possible session states."""

from enum import Enum


class SessionState(Enum):
    NOT_STARTED = "not_started"
    ACTIVE = "active"
    STOPPED = "stopped"
