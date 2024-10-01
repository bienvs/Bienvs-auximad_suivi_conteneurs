from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Reception(Base):
    __tablename__ = 'reception'
    
    id = Column(Integer, primary_key=True, index=True)
    
    # clé étrangère vers la classe transporteur
    transporteur_id = Column(Integer, ForeignKey('transporteur.id'))
    
    # relation avec la classe transporteur
    trasporteur = relationship('Transporteur', back_populates='expedition')
    
    # relation avec la classe conteneurs
    conteneurs = relationship('Conteneurs', back_populates='expedition')
    
    # relation avec la classe Documents
    documents = relationship('Documents', back_populates='expedition')
    
    # relation avec la classe DocumentReception
    documents_reception = relationship('DocumentReception', back_populates='reception')
    
    # relation avec la classe Notification
    documents_expedition = relationship('Notifier', back_populates='expedition')