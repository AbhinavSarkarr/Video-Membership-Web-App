from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid
from app.config import get_settings
from app.users import validators


settings = get_settings()


class User(Model):
    __keyspace__ = settings.keyspace

    email: columns.Text = columns.Text(primary_key=True)
    user_id: columns.UUID = columns.UUID(primary_key=True, default=uuid.uuid1)
    password: columns.Text = columns.Text()


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"
    
    @staticmethod
    def create_user(email, password=None):
        q = User.objects.filter(email=email)
        if q != 0:
            raise Exception("This Email is already registered")
        valid, msg, email = validators._validate_email(email)
        if not valid:
            raise Exception(f"Invalid Email: {msg}") 
        obj = User(email=email)
        obj.password = password
        obj.save()
        return obj
