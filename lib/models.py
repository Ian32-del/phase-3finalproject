from sqlalchemy import   Column , Integer , String ,ForeignKey, create_engine
from sqlalchemy.orm import relationship , backref
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class User (Base):
    __tablename__= 'users'

    id = Column (Integer(), primary_key=True)
    name = Column (String())

    transactions = relationship('Transaction' , backref='user')

    def __repr__(self):
        return f"{self.id} {self.name}"

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer() , primary_key=True)
    amount = Column (Integer())
    user_id = Column(Integer() , ForeignKey('users.id'))



# engine = create_engine ('sqlite:///transaction.db')
# create a databaase engine 


# Base.metadata.create_all(engine) 
# Create the tables in the database






