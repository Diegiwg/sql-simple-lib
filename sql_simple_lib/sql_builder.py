from typing import Optional


class SQLBuilder:
    def __init__(self) -> None:
        self._from = str()
        self._select = str("*")

    def __repr__(self) -> str:
        return self.CODE()

    def CODE(self):
        return f"{self._select}\n{self._from};"

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

                field_value = field_value.strip()
                field_name = field_name.strip()

                if field_value.find("{") == -1:
                    m_fields.append(f"{field_value} AS [{field_name}]")

                else:
                    m_multi_field = []
                    for _ in range(field_value.count("{")):
                        _start = field_value.find("{")
                        _end = field_value.find("}")

                        _name = field_value[_start + 1 : _end]
                        _value = field_value[:_start]

                        m_multi_field.append(f"'{_value}'")
                        m_multi_field.append(_name)

                        field_value = field_value[_end + 1 :]

                    m_fields.append(f"{' + '.join(m_multi_field)} AS [{field_name}]")

        m_fields_compiled = ", ".join(m_fields)
        self._select = f"SELECT {m_fields_compiled}"

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
