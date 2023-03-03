from typing import Optional


class SQLBuilder:
    def __init__(self) -> None:
        self._from = str()
        self._select: list[str] = list()

    def __repr__(self) -> str:
        return self.CODE()

    def CODE(self):
        _select = f"SELECT {', '.join(self._select if len(self._select) > 0 else '*')}"

        return f"{_select}\n{self._from};"

    def SELECT(self, *fields: str):
        """The SELECT command is used to select data from a database.
        The data returned is stored in a result table, called the result set."""

        if not fields:
            raise ValueError("SELECT requires at least one field")

        for field in fields:
            if not isinstance(field, str) or field == "":
                raise ValueError("SELECT requires all fields to be strings")

            # FIXME: field can be complex, with the `=` marker to define an AS, and `__text__ {field} __text__` to define a string formatting.
            self._select.append(field)

    def FROM(self, table_name: str, as_name: Optional[str] = None):
        """The FROM command is used to specify which table to select or delete data from."""

        if not isinstance(table_name, str) or table_name == "":
            raise ValueError("table_name must be a non-empty string")

        if as_name:
            if not isinstance(as_name, str) or as_name == "":
                raise ValueError("as_name must be a non-empty string")

            self._from = f"FROM {table_name} AS {as_name}"
            return

        # TODO: Implement option for multiple tables, with AS command being possible.

        self._from = f"FROM {table_name}"
