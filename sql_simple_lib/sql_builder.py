class SQLBuilder:
    def __init__(self) -> None:
        self._from = str()
        self._select = str("*")

    def __repr__(self) -> str:
        return self.CODE()

    def CODE(self):
        _from = f"FROM {self._from}"

        return f"{self._select}\n{_from};"

    def SELECT(self, *fields: str):
        """The SELECT command is used to select data from a database.
        The data returned is stored in a result table, called the result set."""

        if not fields:
            raise ValueError("SELECT requires at least one field")

        m_fields: list[str] = list()
        for field in fields:
            if not isinstance(field, str) or field == "":
                raise ValueError("SELECT requires all fields to be strings")

            if field.find("=") == -1:
                m_fields.append(field)

            else:
                field_value, field_name = field.split("=")

                # TODO: Implement multi-field `string formatting` support in a single AS command.
                field_value = field_value.replace("{", "").replace("}", "")

                m_fields.append(f"{field_value.strip()} AS [{field_name.strip()}]")

        m_fields_compiled = ", ".join(m_fields)
        self._select = f"SELECT {m_fields_compiled}"

    def FROM(self, table_name: str):
        """The FROM command is used to specify which table to select or delete data from."""

        if not isinstance(table_name, str) or table_name == "":
            raise ValueError("table_name must be a non-empty string")

        # FIXME: table_name can be complex, with the `=` marker to define an AS.
        self._from = table_name
