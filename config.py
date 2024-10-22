from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///suivi_conteneurs.db"
settings = {
    "EMAIL_HOST" : "",
    "EMAIL_PORT" : "",
    "EMAIL_HOST_USER" : "",
    "EMAIL_HOST_PASSWORD" : "",
    "EMAIL_USE_TLS" : "",
    "EMAIL_USE_SSL" : "",
    "EMAIL_TIMEOUT" : "",
    "EMAIL_SSL_KEYFILE" : "",
    "EMAIL_SSL_CERTFILE" : "",
    "DEFAULT_CHARSET" : ""
}

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

def create_session():
    return SessionLocal()