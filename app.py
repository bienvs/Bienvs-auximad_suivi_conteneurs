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
from models.document_expedition import DocumentExpedition
from models.expedition import Expedition

from datetime import datetime

# creation de l'engine
engine = create_engine(DATABASE_URL)

# creation de la session
Session = sessionmaker(bind=engine)
session = Session()

def test_database():
    # Conteneur.__table__.drop(engine)
    # DocumentEnlevement.__table__.drop(engine)
    # Document.__table__.drop(engine)
    # Transporteur.__table__.drop(engine)
    Enlevement.__table__.drop(engine)
    # DocumentExpedition.__table__.drop(engine)
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
    eta_date = "2024-05-06"
    sur_date = "2024-05-06"
    sur_date = "2024-05-06"
    mag_date = "2024-05-06"
    nouvel_enlevement = Enlevement(
        date_enlevement = datetime.strptime(date_string4, '%Y-%m-%d').date(),
        lieu_enlevement = "Tamatave",
        ETA = datetime.strptime(eta_date, '%Y-%m-%d').date(),
        date_surestaries = datetime.strptime(sur_date, '%Y-%m-%d').date(),
        depassement_jours = "0",
        surestaries = "0",
        date_magasinage = datetime.strptime(mag_date, '%Y-%m-%d').date(),
        frais_magasinage = "0",
        document = [nouveau_document],
        transporteur = nouveau_transporteur,
        conteneur = [nouveau_conteneur],
        enlevement_document = [nouveau_document_enlevement]
    )

    # Ajout de l'enlevement à la session
    session.add(nouvel_enlevement)
    session.commit()
    
    session.refresh(nouvel_enlevement) # rafraichir pour obtenir l'id de l'enleevement
    print("Enlevement  créé avec succés!")    

    # ----------------------------------------------------- creation du document specifier pour l'enlevement -------------------------------------------------------------------
    res_date = "2024-08-02"
    env_date = "2024-08-02"
    nouveau_document_expedition = DocumentExpedition(
        num_bon_de_livraison = "0001",
        date_bon_de_livraison = datetime.strptime(date_string2, '%Y-%m-%d').date(),
        num_dossier = "0001",
        lieu_restitution = "Antsirabe",
        date_restitution = datetime.strptime(res_date, '%Y-%m-%d').date(),
        date_envoi = datetime.strptime(env_date, '%Y-%m-%d').date(),
        envoi_a = "Tamatave"
    )
    
    # Ajout des documents specifiés pour l'enlevement à la session
    session.add(nouveau_document_expedition)
    
    session.commit()
    print('Document pour expedition ajouté avec succés!')
    
    # ----------------------------------------------------- creation de l'expédition -------------------------------------------------------------------
    eir_date = "2024-08-02"
    nouvelle_expedition = Expedition(
        num_de_livraison = "001",
        num_EIR_plein = "001",
        date_EIR_plein = datetime.strptime(eir_date, '%Y-%m-%d').date(),
        documents_expedition = [nouveau_document_expedition],
        enlevement = nouvel_enlevement,
    )
    
    # Ajout des expedition à la session
    session.add(nouvelle_expedition)
    session.commit()
    
    session.refresh(nouvelle_expedition)
    print('Expedition ajouté avec succés!')
    
    # afficher l'information du bon de sortie
    bon_de_sortie_info = nouvelle_expedition.get_bon_sortie_info()
    
    # afficher l'informartion du transporteur
    transporteur_info = nouvelle_expedition.get_transporteur_info()
    
    # afficher l'information du conteneur
    conteneur_info = nouvelle_expedition.get_conteneur_info()
    
test_database()