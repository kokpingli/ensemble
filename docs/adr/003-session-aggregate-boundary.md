# ADR-003: Session Aggregate Boundary

## Context
Session manages its own state and maintains data consistency (unique pieces, session lifecycle, state transitions) to provide a reliable practice experience. This logic belongs in the domain to keep the model coherent.

## Decision
Session will be modeled as an aggregate root to enforce business invariants and manage session state consistency.

## Consequences
- Business logic centralized in Session domain entity
- Session manages its own state transitions and validation
- Requires aggregate repository pattern for persistence

## Status
Accepted