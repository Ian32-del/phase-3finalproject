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

    first_user = User(name='Ian Odhiambo')
    first_transaction = Transaction(amount=250,user=first_user)

    second_user = User ( name = 'Rob Tom')
    second_transaction = Transaction(amount=300,user=second_user)


    session.add(new_user)
    session.add(new_transaction)

    session.add(first_user)
    session.add(first_transaction)

    session.add(second_user)
    session.add(second_transaction)


    session.commit()