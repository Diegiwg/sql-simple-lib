from sql_builder import SQLBuilder

sql_builder = SQLBuilder()

sql_builder.SELECT("a", "b", "c")
sql_builder.FROM("users")
print(sql_builder)
