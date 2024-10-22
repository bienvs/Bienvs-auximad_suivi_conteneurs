from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class DocumentExpedition(Base):
    __tablename__ = 'documents_expedition'
    
    id = Column(Integer, primary_key=True, index=True)
    num_bon_de_livraison = Column(String, nullable=False)
    date_bon_de_livraison = Column(Date, nullable=False)
    num_dossier = Column(String, nullable=False)
    lieu_restitution = Column(String, nullable=False)
    date_restitution = Column(Date, nullable=False)
    date_envoi = Column(Date, nullable=False)
    envoi_a = Column(String, nullable=False)
    
    # clé étrangère pour l'expédition
    expedition_id = Column(Integer, ForeignKey('expedition.id'))
    # Relation avec la classe Expedition
    expedition = relationship('Expedition', back_populates='documents_expedition')