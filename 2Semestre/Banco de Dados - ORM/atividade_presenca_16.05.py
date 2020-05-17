import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()


Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO (
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255) NOT NULL,
                        PAGINAS INT NOT NULL,
                        AUTOR_ID INT NOT NULL)""")


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


aut1 = Autor('R. R. Martin')
aut2 = Autor('Stephen King')
lista = [aut1, aut2]
session.add_all(lista)
session.commit()

liv1 = Livro('A Dance with Dragons', 1112, aut1.id)
liv2 = Livro('It - A Coisa', 1104, aut2.id)
lista2 = [liv1, liv2]
session.add_all(lista2)
session.commit()


print('-'*30)
result = session.query(Autor).all()
for i in result:
    print('ID: ', i.id, '\nAutor: ', i.nome, '\n')

print('-'*30)
result = session.query(Livro).all()
for i in result:
    print('\nID: ', i.id, '\nTítulo: ', i.titulo, '\nPáginas: ',
          i.paginas, '\nAutor: ', session.query(Autor).get(i.autor_id).nome)

connection.close()
