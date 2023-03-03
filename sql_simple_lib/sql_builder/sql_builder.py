from typing import Optional

from .commands.From import From
from .commands.Select import Select


class SQLBuilder:
    def __init__(self) -> None:
        self._from = str()
        self._select = str("*")

        self.FROM = From(self).execute
        self.SELECT = Select(self).execute

    def __repr__(self) -> str:
        return self.CODE()

    def CODE(self):
        return f"{self._select}\n{self._from};"
