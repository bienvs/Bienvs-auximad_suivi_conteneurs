from sqlalchemy import create_engine
from models import Base
from config import DATABASE_URL


# Créer le moteur de la base de données en utilisant l'URL de la base de données
engine = create_engine(DATABASE_URL)

# Créer toutes les tables dans la base de données
Base.metadata.create_all(bind=engine)

print("Base de données et tables créées avec succès!")
