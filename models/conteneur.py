from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base
import enum

class EtatTCEnum(enum.Enum):
    FULL_IN = "Full In"
    EMPTY_IN = "Empty In"

class ConteneurType(enum.Enum):
    TWENTY_FT = "20ft"
    FORTY_FT = "40ft"
    REEFER = "Reefer"
class Conteneurs(Base):
    __tablename__ = 'conteneurs'
    
    id = Column(Integer, primary_key=True, index=True)
    num_TC = Column(String, nullable=False)
    plomb = Column(String, nullable=False)
    type_conteneur = Column(Enum(ConteneurType), nullable=False)
    etat_TC = Column(Enum(EtatTCEnum), nullable=False)
    observation = Column(String, nullable=False)
    num_BL = Column(String, nullable=False)
    compagnie_de_navigation = Column(String, nullable=False, default=EtatTCEnum.EMPTY_IN)
    
    
    # clé étrangère pour l'enlevement
    enlevement_id = Column(Integer, ForeignKey('enlevement.id'))
    
    # relation avec l'enlevement
    enlevement = relationship('Enlevement', back_populates='conteneurs')