import pandas as pd
import sys
import numpy as np

import csv

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex1.csv"
# df = pd.read_csv(file_name)
# print(df)

# df1 = pd.read_table(file_name, sep=',')
# print(df1)

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex2.csv"
# df2 = pd.read_csv(file_name, header=None)
# print(df2)

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex2.csv"
# df3 = pd.read_csv(file_name, names = ['a', 'b', 'c', 'd', 'message'])
# print(df3)

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/csv_mindex.csv"
# parsed = pd.read_csv(file_name, index_col=[ 'key1', 'key2'])
# print(parsed)

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex3.txt"
# print(list(open(file_name)))
# result = pd.read_table(file_name, sep='\s+')
# print(result)

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex4.csv"  
# result = pd.read_csv(file_name, skiprows=[0, 2, 3])
# print(result)

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex5.csv"  
# result = pd.read_csv(file_name)
# print(result)
# print(pd.isnull(result))

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex6.csv"  
# # result = pd.read_csv(file_name, nrows=5)
# # print(result)

# chunker = pd.read_csv(file_name, chunksize=1000)
# print(chunker)

# # tot = pd.Series([]) #Error
# tot = pd.Series([], dtype='float64') 
# for piece in chunker:
#     print("piece :", piece)
#     tot = tot.add(piece['key'].value_counts(), fill_value=0)

# tot = tot.sort_values(ascending=False)
# print(tot[:10])

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex5.csv"  
# data = pd.read_csv(file_name)
# # print(data)

# data.to_csv('out.csv')
# data.to_csv(sys.stdout, sep='|') 
# data.to_csv(sys.stdout, na_rep='NULL') 
# data.to_csv(sys.stdout, index=False, header=False)  
# data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])  

# dates = pd.date_range('1/1/2000', periods=7)
# ts = pd.Series(np.arange(7), index=dates)
# ts.to_csv("TSeries.csv")

# file_name = "pydata-book-3rd-edition/pydata-book-3rd-edition/examples/ex7.csv"  
# f = open(file_name)
# reader = csv.reader(f)

# for line in reader:
#     print( line)

# with open(file_name) as f:
#     lines = list(csv.reader(f))

# header, values = lines[0], lines[1:]
# print("values", values)
# print("*values", *values)
# print("zip(*values)", list(zip(*values)))

# data_dict = {h: v for h, v in zip(header, zip(*values))}
# print(data_dict)

# obj = """
# {"name": "wes",
# "places_lived" ["United states", "Spain", "Germany"],
# "pet": null,
# "siblings": [{"ame":Scott}]

# }
# """


# import sqlalchemy as sqla
# from sqlalchemy import text as sql_text
# db = sqla.create_engine("sqlite:///mydata.sqlite")
# # conn = db.connect()
# query = "SELECT * FROM test"
# # pd.read_sql(, db)
# df = pd.read_sql_query(con=db.connect(), sql=sql_text(query))


# import sqlite3

# query = """
# CREATE TABLE test
# (a VARCHAR(20), b VARCHAR(20),
#  c REAL,        d INTEGER
# );"""

# con = sqlite3.connect("mydata.sqlite")
# con.execute(query)
# con.commit()


# data = pd.DataFrame(np.arange(12).reshape((3, 4)),
#                     index=["Ohio", "Colorado", "New York"],
#                     columns=["one", "two", "three", "four"])


# def transform(x):
#     return x[:4].upper()

# print(data.index.map(transform))



ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
age_categories = pd.cut(ages, bins)
print(age_categories)
