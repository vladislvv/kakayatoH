from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy.orm import registry

# говорят перенести в .env файл
engine = create_engine("sqlite:///:memory:")
mapper_registry = registry()

users = Table(
    "users",
    mapper_registry.metadata,

    Column("id", Integer(), primary_key=True),
    Column("firstname", String()),
    Column("lastname", String()),
    Column("mail", String(), unique=True)
)


class User:
    pass


mapper_registry.map_imperatively(User,users)

mapper_registry.metadata.create_all(bind=engine)
