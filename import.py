import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



os.environ["DATABASE_URL"] = "postgres://xgqjlgqhllptkx:b0c038bec42ebc57dc2b89fb87447625e20ffd4e7eb5e2589831e7910ae84258@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/d88oobt5q6ppat"
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

with open("books.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": line[0], "title": line[1], "author": line[2], "year": line[3]})
    db.commit()
        