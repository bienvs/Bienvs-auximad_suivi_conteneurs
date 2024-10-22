from sqlalchemy import Column, Integer, String,Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Expedition(Base):
    __tablename__ = 'expedition'
    
    id = Column(Integer, primary_key=True, index=True)
    num_de_livraison = Column(String, nullable=False)
    num_EIR_plein = Column(String, nullable=False)
    date_EIR_plein = Column(Date, nullable=False)
    
    # clé étrangère vers la classe transporteur
    # transporteur_id = Column(Integer, ForeignKey('transporteur.id'))
    
    # relation avec la classe transporteur
    # trasporteur = relationship('Transporteur', back_populates='expedition')
    
    # relation avec la classe conteneurs
    # conteneurs = relationship('Conteneurs', back_populates='expedition')
    
    # relation avec la classe Documents
    # documents = relationship('Documents', back_populates='expedition')
    
    # relation avec la classe DocumentExpedition
    documents_expedition = relationship('DocumentExpedition', back_populates='expedition')
    
    # relation avec la classe Notification
    # documents_expedition = relationship('Notifier', back_populates='expedition')
    
    # clé étrangères vers la classe enlevement
    enlevement_id = Column(Integer, ForeignKey('enlevement.id'))
    
    # relation avec la classe enlevement
    enlevement = relationship('Enlevement', back_populates = 'expedition')
    
    def get_bon_sortie_info(self):
        """
        Récupère les informations du bon de sortie et le numéro dossier de l'enlèvement assoscié
        """
        
        for document in self.enlevement.document:
            print(document.date_bon_de_sortie)
            print(document.num_dossier)
            return {
                "date_de_bon_de_sortie": document.date_bon_de_sortie,
                "num_dossier": document.num_dossier,
            }
            
    def get_transporteur_info(self):
        """
        Récupère les informations du transporteur de l'enlevement
        """
        print(self.enlevement.transporteur.nom_transporteur)
        return {
            "nom_transporteur": self.enlevement.transporteur.nom_transporteur,
            "nom_chauffeur": self.enlevement.transporteur.nom_chauffeur,
            "permis_de_conduire": self.enlevement.transporteur.permis_de_conduire,
            "num_telephone": self.enlevement.transporteur.num_telephone,
            "num_camion": self.enlevement.transporteur.num_camion,
            "num_remorque": self.enlevement.transporteur.num_remorque,
        }
        
    def get_conteneur_info(self):
        """ 
        Récupère les informations du conteneur
        """
        for conteneur in self.enlevement.conteneur:
            print(conteneur.etat_TC)
            return {
                "plomb": conteneur.plomb,
                "type_conteneur": conteneur.type_conteneur,
                "etat_TC": conteneur.etat_TC,
                "observation": conteneur.observation,
                "num_BL": conteneur.num_BL,
                "compagnie_de_navigation": conteneur.compagnie_de_navigation,
            }
