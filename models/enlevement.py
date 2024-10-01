from sqlalchemy import Column, Integer, String,DateTime, ForeignKey, Double
from sqlalchemy.orm import relationship
from .base import Base

class Enlevement(Base):
    __tablename__ = 'enlevement'
    
    id = Column(Integer, primary_key=True, index=True)
    date_enlevement = Column(DateTime, nullable=False)
    lieu_enlevement = Column(String, nullable=False)
    ETA = Column(String, nullable=False)
    date_surestaries = Column(String, nullable=False)
    depassement_jours = Column(String, nullable=False)
    surestaries = Column(Double, nullable=False, default='0.00')
    date_magasinage = Column(String, nullable=False)
    frais_magasinage = Column(Double, nullable=False, default='0.00')
    
    # clé étrangère vers la classe transporteur
    transporteur_id = Column(Integer, ForeignKey('transporteur.id'))
    
    # relation avec la classe transporteur
    trasporteur = relationship('Transporteur', back_populates='enlevement')
    
    # relation avec la classe conteneurs
    conteneurs = relationship('Conteneurs', back_populates='enlevement')
    
    # relation avec la classe Documents
    documents = relationship('Documents', back_populates='enlevement')
    
    # relation avec la classe DocumentEnlevement
    documents_enlevement = relationship('DocumentEnlevement', back_populates='enlevement')
    
    # relation avec la classe AutresDocuments
    autres_documents = relationship('AutresDocuments', back_populates='enlevement')