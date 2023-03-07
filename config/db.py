# from sqlalchemy import MetaData, create_engine

# engine = create_engine("mysql+pymysql://root@localhost:3306/py_crud")


# meta = MetaData()

# conn = engine.connect()


import pymysql

# database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="py_crud")
conn = connection.cursor()
# some other statements  with the help of cursor
connection.close()