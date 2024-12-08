from assimilator.alchemy import AlchemyUnitOfWork
from assimilator.alchemy.database import AlchemyRepository
from assimilator.core.database import Repository, UnitOfWork
from assimilator.core.services import CRUDService
from sqlalchemy.orm import sessionmaker

from database import engine, User

DatabaseSession = sessionmaker(engine)

def get_repository() -> Repository:
   return AlchemyRepository(
        session =DatabaseSession(),
        model=User
    )


def get_uow() -> UnitOfWork:
    return AlchemyUnitOfWork(
        repository=get_repository()

    )
def get_crud()-> CRUDService:
    return  CRUDService(uow=get_uow())

