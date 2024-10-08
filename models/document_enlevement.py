from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class DocumentEnlevement(Base):
    """
    table pour les documents specifier pour la phase enlèvement
    """
    __tablename__ = 'enlevement_document'
    id = Column(Integer, primary_key=True, index=True)
    # id = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    ref_get_pass = Column(String, nullable=False)
    date_get_pass = Column(Date, nullable=False)
    ref_BAD = Column(String, nullable=False)
    date_BAD = Column(Date, nullable=False)
    
    # clé étrangère pour l'enlevement
    enlevement_id = Column(Integer, ForeignKey('enlevement.id'))
    
    # Relation avec la classe Enlevement
    enlevement = relationship('Enlevement', back_populates='enlevement_document')
