from sqlalchemy import Column, Integer, String,DateTime, ForeignKey, Double
from sqlalchemy.orm import relationship
from .base import Base

class Enlevement(Base):
    """
    classe pour la phase Enlevement
    """
    __tablename__ = 'enlevement'
    
    id = Column(Integer, primary_key=True, index=True)
    date_enlevement = Column(DateTime, nullable=False)
    lieu_enlevement = Column(String, nullable=False)
    ETA = Column(String, nullable=False, default='0.00')
    date_surestaries = Column(String, nullable=False, default=None)
    depassement_jours = Column(String, nullable=False, default=None)
    surestaries = Column(Double, nullable=False, default='0.00')
    date_magasinage = Column(String, nullable=False, default=None)
    frais_magasinage = Column(Double, nullable=False, default='0.00')
    
    # relation avec la classe transporteur
    document = relationship('Document', back_populates='enlevement', cascade="all, delete-orphan")
    
    # clé étrangère vers la classe transporteur
    transporteur_id = Column(Integer, ForeignKey('transporteur.id'))
    
    # relation avec la classe transporteur
    transporteur = relationship('Transporteur', back_populates='enlevement')
    
    # relation avec la classe conteneurs
    conteneur = relationship('Conteneur', back_populates='enlevement', cascade="all, delete-orphan")
    
    # relation avec la classe DocumentEnlevement
    enlevement_document = relationship('DocumentEnlevement', back_populates='enlevement', cascade="all, delete-orphan")
    
    # relation avec la classe AutresDocuments
    # autres_documents = relationship('AutresDocuments', back_populates='enlevement')