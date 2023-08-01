from sqlalchemy import create_engine
from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime


engine = create_engine('postgresql://postgres:root@localhost/pythondb')

metadata = MetaData() # Aquí se crea una instancia del objeto MetaData

#users

users = Table(
    'users', # Nombre de la tabla
    metadata, # Objeto de tipo metadato
    Column('id', Integer(), primary_key=True), # Creamos las columnas
    Column('username', String(), index=True, nullable=False), # Creamos las columnas
    Column('email', String(), nullable=False), # Creamos las columnas
    Column('created_at', DateTime(), default=datetime.now()), # Creamos las columnas
)

            
if __name__ == '__main__':
    
    metadata.create_all(engine)
    
    
    