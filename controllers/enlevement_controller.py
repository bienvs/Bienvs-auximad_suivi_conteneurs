from sqlalchemy.orm import Session
from models.enlevement import Enlevement
from models.document import Document
from models.transporteur import Transporteur
from models.conteneur import Conteneur
from models.document_enlevement import DocumentEnlevement
from views.enlevement_view import EnlevementView

class EnlevementController:
    """
    le controleur de la phase enlevement
    """
    
    def __init__(self, session: Session, view: EnlevementView):
        self.session = session
        self.view = view
        
    # connecter le bouton à la méthode de création de d'enlèvement
        self.view.btn_valider.clicked.connect(self.creer_enlevement)
        
    def creer_enlevement(self):
        """
        creer un nouvel enlevement, recuperer les data et enregistrer dans la BD
        """
        print("creer un nouvel enlevement")
        
        # Récupère les données depuis l'interface 
        document_data = self.view.get_document_data()
        print(document_data)
        enlevement_specific_document_data = self.view.get_enlevement_specific_document_data()
        print(enlevement_specific_document_data)
        conteneur_data = self.view.get_conteneur_data()
        print(conteneur_data)
        transporteur_data = self.view.get_transporteur_data()
        print(transporteur_data)
        date_lieu_enlevement = self.view.get_date_lieu_enlevement()
        print(date_lieu_enlevement)
        
        # fusionner les documents
        # full_document_data = {**document_data, **enlevement_specific_document_data}
        # créer les objets associées 
        enlevement_document = DocumentEnlevement(**enlevement_specific_document_data)
        document = Document(**document_data)
        conteneur = Conteneur(**conteneur_data)
        transporteur = Transporteur(**transporteur_data)
        
        # creer l'objet enlevement 
        nouvel_enlevement = Enlevement(
            date_lieu_enlevement = date_lieu_enlevement,
            document = [document],
            transporteur = transporteur,
            conteneur = [conteneur],
            enlevement_document = [enlevement_document]
        )
        
        # sauvegarde dans la BD
        try:
            self.session.add(nouvel_enlevement)
            self.session.commit()
            self.session.close()
            print("enlèvement cree avec succes")
            
        except Exception as e:
            self.session.rollback()
            print(f"erreur lors de la creation de l'enlevement: {e}")
        
        
        # Réinitialise le formulaire
        