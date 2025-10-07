"""Repository interface for Section aggregate."""

from abc import ABC, abstractmethod

from .section import Section


class SectionRepository(ABC):
    """Abstract repository for Section persistence."""

    @abstractmethod
    def get_by_id(self, section_id: str) -> Section:
        """Retrieve a section by its unique identifier."""

    @abstractmethod
    def save(self, section: Section) -> None:
        """Persist a section to storage."""
