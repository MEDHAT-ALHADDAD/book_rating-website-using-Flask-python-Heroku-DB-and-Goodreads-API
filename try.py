import csv
import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
# if not os.getenv(""):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("")
db = scoped_session(sessionmaker(bind=engine))


def main():
    name = "%"+"Krondor"+"%"
    books = db.execute("SELECT * FROM books WHERE (isbn LIKE :name  OR title LIKE :name OR author LIKE :name) ", {"name": name}).fetchall()
    for book in books:
        print(book)


if __name__ == '__main__':
    main()
