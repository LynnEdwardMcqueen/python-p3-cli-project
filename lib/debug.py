#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Recipe

if __name__ == '__main__':
    engine = create_engine('sqlite:///recipes.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    recipe_list = session.query(Recipe).all()

    import ipdb; ipdb.set_trace()