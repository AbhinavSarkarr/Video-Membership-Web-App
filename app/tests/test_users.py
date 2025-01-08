import pytest
from app.users.models import User
from app import db


@pytest.fixture(scope='module')
def setup_session():
    session = db.get_session()
    yield session
    q = User.objects.filter(email='test@test.com')
    if q.count() != 0:
        q.delete()
    session.shutdown()


def test_create_user(setup_session):
    User.create_user(email='test@test.com', password="12345")

def test_invalid_email(setup_session):
    with pytest.raises(Exception):
        User.create_user(email='test@test.com', password="12345")

def test_valid_password(setup_session):
    q = User.objects.filter(email='test@test.com')
    assert q.count() == 1
    user_obj = q.first()
    assert user_obj.verify_password("12345") == True
    assert user_obj.verify_password("123456") == False