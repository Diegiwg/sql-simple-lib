# SQL Simple Lib

> A library to write SQL code in a different way

## Goal's

1. Learn SQL by writing an educational library.
2. Facilitate access to writing SQL code, with functions in Portuguese.

## Current version use

`example.py`

```python
from sql_builder import SQLBuilder

sql_builder = SQLBuilder()

sql_builder.SELECT("o.OrderID = Order", "Client: {c.CustomerName} = Name")
sql_builder.FROM("Customers = c", "Orders = o")

print(sql_builder)
```

`std::out`

```sql
SELECT o.OrderID AS [Order], 'Client: ' + c.CustomerName AS [Name]
FROM Customers AS c, Orders AS o;
```

> Tested on `https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_alias_column2&ss=-1`, with output:
>
> | Order | Name |
> | ----------- | ----------- |
> |10248 | Client: Alfreds Futterkiste |
> |10248 | Client: Ana Trujillo Emparedados y helados |
>  
