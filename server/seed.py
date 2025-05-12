#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Earthquake

with app.app_context():

    # Delete all rows in the "earthquakes" table
    Earthquake.query.delete()
    Earthquake.query.delete()

    # Add several Earthquake instances to the "earthquakes" table
    earthquakes = [
        Earthquake(magnitude=7.8, location="Nepal", year=2015),
        Earthquake(magnitude=9.1, location="Sumatra", year=2004),
        Earthquake(magnitude=8.0, location="Peru", year=2007),
        Earthquake(magnitude=7.6, location="Pakistan", year=2005),
        Earthquake(magnitude=8.1, location="Mexico", year=2017)
    ]
    db.session.add_all(earthquakes)
    db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960))
    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964))
    db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946))
    db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934))
    db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922))

    # Commit the transaction
    db.session.commit()
    db.session.commit()
