# ADR-002: Multiple Pieces Per Session

## Context
Real practice sessions involve working on multiple pieces (e.g., difficult Bach passage, then complete Dvorak piece). Forcing "1 session = 1 piece" would bend reality to fit the software framework rather than having the software reflect reality.

## Decision
A session can contain multiple pieces.

## Consequences
- Session can track realistic practice workflows across multiple pieces
- Users can switch pieces without creating new sessions
- Requires Session to manage piece collection and current piece state
- Adds complexity to session transitions and state management

## Status
Accepted