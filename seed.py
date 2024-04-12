"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import app, db  # Ensure 'app' is imported here
from models import User, Message, Follows

# Place all operations inside the application context
with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Open and read the users.csv file and insert into User model
    with open('generator/users.csv') as users:
        db.session.bulk_insert_mappings(User, DictReader(users))

    # Open and read the messages.csv file and insert into Message model
    with open('generator/messages.csv') as messages:
        db.session.bulk_insert_mappings(Message, DictReader(messages))

    # Open and read the follows.csv file and insert into Follows model
    with open('generator/follows.csv') as follows:
        db.session.bulk_insert_mappings(Follows, DictReader(follows))

    # Commit all changes to the database
    db.session.commit()