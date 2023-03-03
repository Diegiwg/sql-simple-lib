from sql_builder import SQLBuilder

sql_builder = SQLBuilder()

sql_builder.SELECT("a", "b", "c")
sql_builder.FROM("users", "u")
print(sql_builder)
