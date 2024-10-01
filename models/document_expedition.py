from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .document import Document

class DocumentExpedition(Document):
    __tablename__ = 'documents_expedition'
    
    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    num_bon_de_livraison = Column(String, nullable=False)
    date_bon_de_livraison = Column(Date, nullable=False)
    num_dossier = Column(String, nullable=False)
    lieu_restitution = Column(String, nullable=False)
    date_restitution = Column(Date, nullable=False)
    date_envoi = Column(Date, nullable=False)
    envoi_a = Column(String, nullable=False)
    
    # Relation avec la classe Expedition
    expedition = relationship('Expedition', back_populates='documents_expedition')