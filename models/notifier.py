from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Notifier(Base):
    __tablename__ = 'notifier'

    id = Column(Integer, primary_key=True, index=True)
    adresse_email = Column(String, nullable=False)
    propietaire = Column(String, nullable=False)
    
    # clé etrangère pour l'expedition
    expedition_id = Column(Integer, ForeignKey('expedition.id'))
    
    # relation avec la classe expedition
    expedition = relationship('Expedition', back_populates='notifier')
    
    # clé etrangère pour la récéption
    reception_id = Column(Integer, ForeignKey('reception.id'))
    
    # relation avec la classe expedition
    reception = relationship('Reception', back_populates='notifier')