from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup_cat import Category, Base, CategoryItem

engine = create_engine('sqlite:///categoryitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Menu for UrbanBurger
category1 = Category(name = "Soccer")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(name = "Shinguards", description = "Shinguards are use to protect the shins", category = category1)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(name = "Two shinguards", description = "Pair of Shinguards", category = category1)

session.add(categoryItem2)
session.commit()


#Menu for Super Stir Fry
category2 = Category(name = "Snowboarding")

session.add(category2)
session.commit()


catItem1 = CategoryItem(name = "Goggles", description = "Goggles for snowboarding", category = category2)

session.add(catItem1)
session.commit()

catItem2 = CategoryItem(name = "Snowboards", description = "Best for any terrain and conditions. All mountain snowboards performa nywhere on a mountain - groomed runs, backcountry, even park and pipe.", category = category2)

session.add(catItem2)
session.commit()





print "added categories and items!"