# initializer for postgresql db with WGS84 storage
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from geoalchemy2 import Geometry


Base = declarative_base()


class ParkingLot(Base):
    __tablename__ = 'parking_lots'

    CarParkID = Column(String, primary_key=True)
    Area = Column(String)
    Development = Column(String)
    AvailableLots = Column(Integer)
    LotType = Column(String)
    Agency = Column(String)
    Location = Column(Geometry(geometry_type='POINT', srid=4326))


engine = create_engine('postgresql://root:root@localhost:5432/sg_carpark')
Base.metadata.create_all(engine)
