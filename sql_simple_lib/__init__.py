from sql_builder import SQLBuilder

sql_builder = SQLBuilder()

sql_builder.SELECT("a=name", "{b} + {c} = data")
sql_builder.FROM("users", "u")

print(sql_builder)
