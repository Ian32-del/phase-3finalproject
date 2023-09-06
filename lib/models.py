from sqlalchemy import ForeignKey , Column , Integer , String , MetaData
from sqlalchemy import relationship ,backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

convection = {
    "fk":"fk_%(table_name)s_%(column_o_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convection)

Base = declarative_base(metadata=metadata)

class transations (Base):

    __tablename__ = 'transactions'

    transactions.id = Column(Integer , primary_keys=True)


