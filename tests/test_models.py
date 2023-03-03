from faker import Faker
from factory import Factory
from pytest import fixture
from pytest import mark
from app.models import DataBase
from app.models import User


class UserFactory(Factory):
    class Meta:
        model = User
    
    username = Faker().name()
    email = Faker().email()
    password = Faker().password()


@fixture(scope='function')
def empty_database():
    database = DataBase(':memory:')
    yield database


@fixture(scope='function')
def database_with_one_user():
    database = DataBase(':memory:')
    user = UserFactory.build()
    database.insert_user(user)
    yield database


def test_get_users_must_return_zero_users(empty_database):
    users = empty_database.get_users()
    assert len(users) == 0


def test_insert_user_must_set_id_to_user(empty_database):
    user = UserFactory.build()
    empty_database.insert_user(user)
    assert user.iduser is not None


def test_get_users_must_return_one_user(database_with_one_user):
    users = database_with_one_user.get_users()
    assert len(users) == 1


def test_filter_users_must_return_one_user(database_with_one_user):
    users = database_with_one_user.filter_users(iduser=1)
    assert len(users) == 1


def test_update_user_must_persist_the_changes_in_username(
    database_with_one_user
):
    old_user = database_with_one_user.get_users()[0]
    old_user.username = Faker().name()
    database_with_one_user.update_user(old_user)
    updated_user = database_with_one_user.get_users()[0]
    assert updated_user.username == old_user.username 

def test_after_delete_all_users_the_database_must_by_empty(
    database_with_one_user
):
    user = database_with_one_user.get_users()[0]
    database_with_one_user.delete_user(user)
    users = database_with_one_user.get_users()
    assert len(users) == 0
