from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///suivi_conteneurs.db"
PATH = 'E:\\Stage\projet_1.0\policy_files\Documents_Légaux\\'

#---------------------------------------------------
SOURCE_MAIL = "mail.auximad.mg"
PWD = ""
ATTEMPT = 3
#---------------------------------------------------

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

def create_session():
    return SessionLocal()