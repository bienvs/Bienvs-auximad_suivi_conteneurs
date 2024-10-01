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
    transporteur_id = Column(Integer, ForeignKey('transporteur.id'))
    
    # relation avec la classe transporteur
    trasporteur = relationship('Transporteur', back_populates='expedition')
    
    # relation avec la classe conteneurs
    conteneurs = relationship('Conteneurs', back_populates='expedition')
    
    # relation avec la classe Documents
    documents = relationship('Documents', back_populates='expedition')
    
    # relation avec la classe DocumentExpedition
    documents_expedition = relationship('DocumentExpedition', back_populates='expedition')
    
    # relation avec la classe Notification
    documents_expedition = relationship('Notifier', back_populates='expedition')