# tester la base de donnees ici...!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models.base import Base
from models.conteneur import Conteneur, ConteneurType, EtatTCEnum
from models.document import Document
from models.transporteur import Transporteur
from models.document_enlevement import DocumentEnlevement
from models.enlevement import Enlevement
from datetime import datetime

# creation de l'engine
engine = create_engine(DATABASE_URL)

# creation de la session
Session = sessionmaker(bind=engine)
session = Session()

def test_database():
    Enlevement.__table__.drop(engine)
    # creation de la table dans la base de donnees
    Base.metadata.create_all(engine)
    
    # ----------------------------------------------------- creation de la conteneur -------------------------------------------------------------------
    nouveau_conteneur = Conteneur(
        num_TC = "12345TC",
        plomb = "123PL",
        type_conteneur = ConteneurType.ISOTANK,
        etat_TC = EtatTCEnum.FULL_IN,
        observation = "Aucune",
        num_BL = "12345BL",
        compagnie_de_navigation = "Maersk",
    )
    
    # ajout du conteneur à la session
    session.add(nouveau_conteneur)
    
    session.commit()
    print("Conteneur ajouté avec succes!")
    
    # ----------------------------------------------------- creation du document-------------------------------------------------------------------
    date_string = "2024-09-17"
    nouveau_document = Document(
        num_bon_de_sortie = "12345BS",
        date_bon_de_sortie = datetime.strptime(date_string, '%Y-%m-%d').date(),
        num_dossier = "0001D",
    )
    
    # Ajout du document à la session
    session.add(nouveau_document)
    
    session.commit()
    print("Document ajouté avec succés!")
    
    # ----------------------------------------------------- creation du transporteur-------------------------------------------------------------------
    nouveau_transporteur = Transporteur(
        nom_transporteur = "transp1",
        nom_chauffeur = "Rakoto",
        permis_de_conduire = "C",
        num_telephone = "033 33 333 33",
        num_camion = "0001 TAB",
        num_remorque = "0001FCB",
    )
    
    # Ajout de la transporteur à la session
    session.add(nouveau_transporteur)
    
    session.commit()
    print('Transporteur ajouté avec succés!')
    
    # ----------------------------------------------------- creation du document specifier pour l'enlevement -------------------------------------------------------------------
    date_string2 = "2024-08-02"
    date_string3 = "2024-08-02"
    nouveau_document_enlevement = DocumentEnlevement(
        ref_get_pass = "0001P",
        date_get_pass = datetime.strptime(date_string2, '%Y-%m-%d').date(),
        ref_BAD = "0001BAD",
        date_BAD = datetime.strptime(date_string3, '%Y-%m-%d').date(),
    )
    
    # Ajout des documents specifiés pour l'enlevement à la session
    session.add(nouveau_document_enlevement)
    
    session.commit()
    print('Document pour enlevement ajouté avec succés!')
    
    # ----------------------------------------------------- creation de l'enlevement -------------------------------------------------------------------
    date_string4 = "2024-08-05"
    nouvel_enlevement = Enlevement(
        date_enlevement = datetime.strptime(date_string4, '%Y-%m-%d').date(),
        lieu_enlevement = "Tamatave",
        document = [nouveau_document],
        transporteur = nouveau_transporteur,
        conteneur = [nouveau_conteneur],
        enlevement_document = [nouveau_document_enlevement]
    )

    # Ajout de l'enlevement à la session
    session.add(nouvel_enlevement)
    session.commit()
    
    print("Enlevem créé avec succés!")    

    
test_database()