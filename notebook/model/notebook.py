from datetime import datetime
from dataclasses import dataclass, field
import uuid


@dataclass
class Note :
    creation_date: datetime = field(default_factory=datetime)
    tags: list[str] = field(default_factory=[])
    code: int
    title: str
    text: str
    importance: str
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __str__(self) -> str :
        return f" Code : {self.code}" \
               f" Creation date : {self.creation_date}" \
               f" {self.title} : {self.text}"

    def add_tag(self, tag: str) :
        if tag not in list[tag] :
            self.tag.append(tag)


class Notebook :

    def __init__(self) :
        pass

    def add_note(self, title: str, text: str, importance: str) :
        new_note = Note(title, text)
        new_note.code = str(uuid.uuid4())
        self.notas.append(new_note)
        return new_note.code

    def important_notes(self) -> list[Note] :
        importance_tag = []
        for x in self.tag :
            if x == "HIGH" or "MEDIUM" :
                x.append(importance_tag)
        return importance_tag

    def tags_note_count(self) -> dict[str, int] :
        dict_tags_count = {}
        for note in self.notes :
            if note.tags :
                for tag in note.tag :
                    dict_tags_count[tag] = dict_tags_count.get(tag, 0) + 1
        return dict_tags_count
