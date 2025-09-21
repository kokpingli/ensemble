graph TB
    subgraph "Session Aggregate"
        SESSION[Session Entity]
    end

    subgraph "Recording Aggregate"
        RECORDING[Recording Entity]
    end

    PIECE[Piece Entity<br/>Simple CRUD]
    CELLIST[Cellist Entity<br/>Simple CRUD]

    SESSION -.-> PIECE
    SESSION -.-> RECORDING
    RECORDING -.-> CELLIST