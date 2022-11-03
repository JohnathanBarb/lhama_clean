from typing import List
from src.data.interfaces import UserRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.domain.models import Users


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    def insert_user(self, name: str, password: str) -> Users:
        """insert data in user entity
        :param - name: user name
               - password: user password
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """Select data in user entity by id and/or name
        :param - user_id: ID of the registry
               - name: user name
        :return - List with Users selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if user_id and not name:

                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]
                elif not user_id and name:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]
                elif user_id and name:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]
                return query_data
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
