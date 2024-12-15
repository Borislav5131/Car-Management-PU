from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Maintenance(Base):
    __tableName__ = "maintenances"
    id = Column(Integer, primary_key=True, index=True)
    serviceType = Column(String),
    scheduleDate = Column(Date),
    carId = Column(Integer)
    carName = Column(String)
    garageId = Column(Integer)
    garageName = Column(String)