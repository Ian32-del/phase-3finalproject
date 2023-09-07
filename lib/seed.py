from faker import Faker
import random


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User , Transaction

if __name__ == '__main__':
    engine = create_engine('sqlite:///transaction.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(User).delete()
    # session.query(Transaction).delete()

    fake = Faker()

    new_user = User(name='John Doe')
    new_transaction = Transaction(amount=100, user=new_user)

    # session.add(new_user)
    # session.add(new_transaction)

    # session.commit()