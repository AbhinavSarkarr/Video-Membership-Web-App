from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection
import json
import pathlib
from . import config

settings = config.get_settings()

BASE_DIR = pathlib.Path(__file__).resolve().parent

ASTRADB_CONNECT_BUNDLE = BASE_DIR / "unencrypted" / "astradb_connect.zip"

def get_session():
    cloud_config= {
    'secure_connect_bundle': ASTRADB_CONNECT_BUNDLE
    }

    CLIENT_ID = settings.client_id
    CLIENT_SECRET = settings.client_secret

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))

    return session


