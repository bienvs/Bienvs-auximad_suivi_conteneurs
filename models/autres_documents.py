from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class AutresDocuments(Base):
    __tablename__ = 'autre_documents'
    
    id = Column(Integer, primary_key=True, index=True)
    code_doc = Column(String, nullable=False)
    libelle = Column(String, nullable=False)
    ref_doc = Column(String, nullable=False)
    date_doc = Column(String, nullable=False)
    
    # clé étrangère pour l'enlevement
    enlevement_id = Column(Integer, ForeignKey('enlevement.id'))
    
    # relation avec la classe enlevement
    enlevement = relationship('Enlevement', back_populates='documents')