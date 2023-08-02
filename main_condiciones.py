import json
from sqlalchemy import create_engine
from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy import select


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
        # SELECT * FROM users WHERE country = 'Serbia';
        select_query = users.select().where(users.c.country == 'Serbia')
        
        # SELECT id, email,name FROM users WHERE country = 'Serbia'
        # select_query = select(
        #     users.c.id,
        #     users.c.email,
        #     users.c.name
        # ).where(
        #     users.c.country == "Serbia"
        # )
        
        print(select_query)
        
        result = connection.execute(select_query) # ResultProxy
        
        for user in result.fetchall():
            # print(user) # RowProxy traerá todos los registros
            print(user) # RowProxy traerá sólo los nombres

        

    