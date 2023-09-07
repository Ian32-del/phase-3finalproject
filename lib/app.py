# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from models import User, Transaction  # Import your User and Transaction models

# # Create a database engine (replace 'sqlite:///your_database.db' with your database URL)
# engine = create_engine('sqlite:///your_database.db')

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Create instances of your models with data
# new_user = User(name='John Doe')
# new_transaction = Transaction(amount=100, user=new_user)

# # Add the objects to the session
# session.add(new_user)
# session.add(new_transaction)

# # Commit the transaction to save the data to the database
# session.commit()

# # Close the session
# session.close()
