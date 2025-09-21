# Entity Relationship Diagram
```mermaid
erDiagram
    SESSION {
        string id
        datetime start_time
        string state
        string cellist_id
    }

    RECORDING {
        string id
        string session_id
        string file_path
        datetime created_at
        string cellist_id
    }

    PIECE {
        string id
        string title
        string composer
    }

    CELLIST {
        string id
        string name
    }

    SESSION ||--o{ PIECE : practices
    SESSION ||--|| RECORDING : generates
    CELLIST ||--o{ SESSION : creates
    CELLIST ||--o{ RECORDING : owns