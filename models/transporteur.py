from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Transporteur(Base):
    """
    table transporteur
    """
    __tablename__ = 'transporteur'
    id = Column(Integer, primary_key=True, index=True)
    nom_transporteur = Column(String, nullable=False)
    nom_chauffeur = Column(String, nullable=False)
    permis_de_conduire = Column(String, nullable=False)
    num_telephone = Column(String, nullable=False)
    num_camion = Column(String, nullable=False)
    num_remorque = Column(String, nullable=False)
    
    # relation avec la classe enlevement
    enlevement = relationship('Enlevement', back_populates='transporteur')
    
    # relation avec la classe expedition
    # expedition = relationship('Expedition', back_populates='transporteur')
    
    # relation avec la classe reception
    # reception = relationship('Reception', back_populates='transporteur')
    
    # relation avec la classe restitution
    # restitution = relationship('Restitution', back_populates='transporteur')
    