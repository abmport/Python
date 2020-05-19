# Abner de Melo Porto
# Vinicius Tertuliano


import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Cria Conexão com o SQLITE.
# Será criado o arquivo server.db no diretório atual
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()


class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    diretor = Column('DIRETOR', String(255))
    ano = Column('ANO', Integer)
    duracao = Column('DURACAO', Integer)
    votos = Column('VOTOS', Integer)
    avaliacao = Column('AVALIACAO', Float)
    genero = Column('GENERO', String(255))

    # Construtor

    def __init__(self, nome, diretor, ano, duracao, votos, avaliacao, genero):
        self.nome = nome
        self.diretor = diretor
        self.ano = ano
        self.duracao = duracao
        self.votos = votos
        self.avaliacao = avaliacao
        self.genero = genero

# Classe para interação com o Banco de Dados


class Banco:
    def criar_tabela(self):
        '''
        Cria a tabela FILME, caso ela não exista no banco de dados
        '''
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255) NOT NULL,
                            DIRETOR VARCHAR(255) NOT NULL,
                            ANO INT NOT NULL,
                            DURACAO INT NOT NULL,
                            VOTOS INT NOT NULL,
                            AVALIACAO FLOAT NOT NULL,
                            GENERO VARCHAR(255) NOT NULL)""")

    def incluir(self, filme: Filme):
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes: list()):
        session.add_all(filmes)
        session.commit()

    def alterar_avaliacao(self, filme: Filme, avaliacao: float):
        alterar = session.query(filme).get(filme.id)
        alterar.avaliacao = avaliacao
        session.commit()

    def excluir(self, id: int):
        excluir = session.query(Filme).get(id)
        if excluir is not None:
            session.delete(excluir)
            session.commit()

    def buscar_todos(self):
        lista = session.query(Filme).order_by(Filme.nome).all()
        return lista

    def buscar_por_id(self, id: int):
        buscar_id = session.query(Filme).get(id)
        return buscar_id

    def buscar_por_ano(self, ano: int):
        buscar_por_ano = session.query(Filme).filter(
            Filme.ano == ano).order_by(Filme.id).all()
        return buscar_por_ano

    def buscar_por_genero(self, genero: str):
        buscar_por_genero = session.query(Filme).filter(
            Filme.genero == genero).order_by(Filme.nome).all()
        return buscar_por_genero

    def buscar_melhores_do_ano(self, ano: int):
        buscar_melhores = session.query(Filme).filter(
            Filme.ano == ano, Filme.avaliacao >= 8.5).order_by(
                desc(Filme.avaliacao))
        return buscar_melhores
