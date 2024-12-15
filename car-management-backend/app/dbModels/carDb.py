from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True, nullable=False)
    model = Column(String, nullable=False)
    production_year = Column(Integer, nullable=False)
    license_plate = Column(String, unique=True, nullable=False)
    garage_id = Column(Integer, ForeignKey("garages.id"), nullable=True)

    garage = relationship("Garage", back_populates="cars")
