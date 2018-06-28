from sqlalchemy import Column, String, Numeric, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    id = Column('id', Integer, primary_key=True)
    contact_phone = Column('contact_phone',  String(50))
    edited_contact_phone = Column('edited_contact_phone', Numeric(15, 0), nullable=True)
