import json
from sqlalchemy import ForeignKey, create_engine
from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime, Float
from sqlalchemy import select, and_, or_
from sqlalchemy import desc, asc, update, delete


engine = create_engine('postgresql://postgres:root@localhost/pythondb')

metadata = MetaData() # Aquí se crea una instancia del objeto MetaData

orders = Table(
    'orders', # Nombre de la tabla
    metadata, # Objeto de tipo metadato
    Column('id', Integer(), primary_key=True), # Creamos las columnas
)

products = Table(
    'products', # Nombre de la tabla
    metadata, # Objeto de tipo metadato
    Column('id', Integer(), primary_key=True), # Creamos las columnas
    Column('title', String()), # Creamos las columnas
    Column('price', Float(5, 2)), # Creamos las columnas
    Column('order_id', ForeignKey('orders.id'))
)



            
if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    connection = engine.connect()
    
    with connection.begin():

        # Orden
        insert_query = orders.insert()
        connection.execute(insert_query)
    
        # Productos
        insert_query = products.insert().values(
            title='Iphone',
            price= 500.50,
            order_id=1
        )
        
        connection.execute(insert_query)
        
        insert_query = products.insert().values(
            title='Ipad',
            price= 800.00,
            order_id=1
        )
        
        connection.execute(insert_query)
        
        insert_query = products.insert().values(
            title='Macbook',
            price= 2000.00,
            order_id=1
        )
        
        connection.execute(insert_query)
        
        
        

        