from typing import Optional


class From:
    def __init__(self, parent) -> None:
        self.parent = parent

    def execute(self, table_name: str, as_name: Optional[str] = None):
        """The FROM command is used to specify which table to select or delete data from."""

        if not isinstance(table_name, str) or table_name == "":
            raise ValueError("table_name must be a non-empty string")

        if as_name:
            if not isinstance(as_name, str) or as_name == "":
                raise ValueError("as_name must be a non-empty string")

            self.parent._from = f"FROM {table_name} AS {as_name}"
            return

        # TODO: Implement option for multiple tables, with AS command being possible.

        self.parent._from = f"FROM {table_name}"
