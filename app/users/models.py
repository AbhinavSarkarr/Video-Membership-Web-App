from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid
from app.config import get_settings
from app.users import validators
from app.users import security


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
    
    def set_password(self, pw, commit=False):
        pw_hash = security.generate_hash(pw)
        self.password = pw_hash
        if commit:
            self.save()
        return True
    
    def verify_password(self, pw_str):
        pw_hash = self.password
        verified, _  = security.verify_hash(pw_hash=pw_hash, pw_raw=pw_str)
        return verified 

    @staticmethod
    def create_user(email, password=None):
        q = User.objects.filter(email=email).count()
        if q != 0:
            raise Exception("This Email is already registered")
        valid, msg, email = validators._validate_email(email)
        if not valid:
            raise Exception(f"Invalid Email: {msg}") 
        obj = User(email=email)
        obj.set_password(password)
        # obj.password = password
        obj.save()
        return obj
