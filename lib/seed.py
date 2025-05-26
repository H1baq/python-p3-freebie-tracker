#!/usr/bin/env python3

# Script goes here!

from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Base
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind = engine)

session =Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

c1 =Company(name="Moringa", founding_year=1997)
c2 = Company(name="Apple", founding_year=1996)

d1 = Dev(name="Alice")
d2 = Dev(name="Bob")

f1 = Freebie(item_name="T-shirt", value=10, dev=d1, company=c1)
f2 = Freebie(item_name="Mug", value=5, dev=d2, company=c1)
f3 = Freebie(item_name="Sticker", value=1, dev=d1, company=c2)

session.add_all([c1, c2, d1, d2, f1, f2, f3])
session.commit()