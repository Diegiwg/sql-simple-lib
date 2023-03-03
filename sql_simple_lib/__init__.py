from sql_builder import SQLBuilder

sql_builder = SQLBuilder()

sql_builder.SELECT("o.OrderID = Order", "Client: {c.CustomerName} = Name")
sql_builder.FROM("Customers = c", "Orders = o")

print(sql_builder)
