from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, index=True)
    num_bon_de_sortie = Column(String, nullable=False)
    date_bon_de_sortie = Column(Date, nullable=False)
    num_dossier = Column(String, nullable=False)
    
    # clé étrangère pour l'enlevement
    enlevement_id = Column(Integer, ForeignKey('enlevement.id'))
    
    # relation avec la classe enlevement
    enlevement = relationship('Enlevement', back_populates='documents')
    
    # clé étrangère pour l'expedition
    expedition_id = Column(Integer, ForeignKey('enlevement.id'))
    
    # relation avec la classe expedition
    expedition = relationship('Enlevement', back_populates='documents')
    