from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .document import Document

class DocumentEnlevement(Document):
    __tablename__ = 'documents_enlevement'
    
    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    ref_get_pass = Column(String, nullable=False)
    date_get_pass = Column(Date, nullable=False)
    ref_BAD = Column(String, nullable=False)
    date_BAD = Column(Date, nullable=False)
    
    # Relation avec la classe Enlevement
    enlevement = relationship('Enlevement', back_populates='documents_enlevement')
