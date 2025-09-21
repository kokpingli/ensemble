# ADR-001: Recording Separate from Session

## Context
Session tracks practice activity metadata while Recording stores valuable audio files. Sessions add cognitive overhead when managing recordings.

## Decision
Recording will be modeled as a separate aggregate from Session with optional SessionId reference.

## Consequences
- Recordings can exist independently (imported files, standalone recordings)
- Users can manage recordings without session complexity
- Cleaner storage separation (metadata vs large audio files)
- Adds nullable SessionId field and potential orphaned references

## Status
Accepted