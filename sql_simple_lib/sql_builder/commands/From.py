from typing import Optional


class From:
    def __init__(self, parent) -> None:
        self.parent = parent

    def execute(self, *table_names: str):
        """The FROM command is used to specify which table to select or delete data from."""

        if not table_names:
            raise ValueError("FROM requires at least one table")

        m_table_names: list[str] = list()
        for table in table_names:
            if not isinstance(table, str) or table == "":
                raise ValueError("table must be a non-empty string")

            if table.find("=") == -1:
                m_table_names.append(f"{table}")

            else:
                table_name, table_alias = table.split("=")

                table_name = table_name.strip()
                table_alias = table_alias.strip()

                m_table_names.append(f"{table_name} AS {table_alias}")

        self.parent._from = f"FROM {', '.join(m_table_names)}"
