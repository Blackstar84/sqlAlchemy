import json
from sqlalchemy import create_engine
from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy import select, and_, or_
from sqlalchemy import desc, asc


engine = create_engine('postgresql://postgres:root@localhost/pythondb')

metadata = MetaData() # Aquí se crea una instancia del objeto MetaData

#users

users = Table(
    'users', # Nombre de la tabla
    metadata, # Objeto de tipo metadato
    Column('id', Integer(), primary_key=True), # Creamos las columnas
    Column('age', Integer(), nullable=False), # Creamos las columnas
    Column('country', String(), nullable=False), # Creamos las columnas
    Column('email', String(), nullable=False), # Creamos las columnas
    Column('gender', String(), nullable=False), # Creamos las columnas
    Column('name', String(), nullable=False), # Creamos las columnas
    Column('created_at', DateTime(), default=datetime.now()), # Creamos las columnas
)



            
if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    connection = engine.connect()
    
    with connection.begin():
        
        insert_query = users.insert()    #Query -> INSERT INTO users
        
        with open('users.json') as file:
            #users = json.load(file)
            connection.execute(users.insert(), json.load(file))
            
        update_query = users.update().where(users.c.id == 1).values(
            name='Cambio de Nombre!'
        )
        
        print(update_query)
        
        result = connection.execute(update_query)
        # Con esto accedemos a la cantidad de filas modificadas
        print(result.rowcount)
        
        update_query = users.update().values(
            name='Cambio de Nombre!'
        )
        
        print(update_query)
        
        result = connection.execute(update_query)
        # Con esto accedemos a la cantidad de filas modificadas
        print(result.rowcount)