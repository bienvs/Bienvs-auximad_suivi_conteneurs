from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base
import enum

class EtatTCEnum(enum.Enum):
    """
    classe enumerer l'option disponible pour l'etat du conteneur
    """
    FULL_IN = "Full In"
    EMPTY_IN = "Empty In"


class ConteneurType(enum.Enum):
    """
    classe enumerer l'option disponible pour le type de conteneur
    """
    FLATRACK_TWENTY = "Flatrack20"
    FLATRACK_FOURTY = "Flatrack40"
    FLATRACKCOL_TWENTY = "FlatrackCol20"
    FLATRACKCOL_FOURTY = "FlatrackCol40"
    ISOTANK = "Isotank"
    OPENTOP_TWENTY = "Opentop20"
    OPENTOP_FOURTY = "Opentop40"
    PLATFORM_TWENTY = "Platform20"
    PLATFORM_FOURTY = "Platform40"
    REEFER_TWENTY = "Reefer20"
    REEFER_FOURTY = "Reefer40"
    REEFER_FOURTY_H = "Reefer40H"
    STANDARD_TWENTY = "Standard20"
    STANDARD_FOURTY = "Standard40"
    UPGRADE_TWENTY = "Upgrade20"
    UPGRADE_FOURTY = "Upgrade40"
    
    
class Conteneur(Base):
    """
    Table conteneur
    """
    __tablename__ = 'conteneur'
    
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
    enlevement = relationship('Enlevement', back_populates='conteneur')
    
    # relation avec Documents
    # document = relationship('Enlevement', back_populates='document')