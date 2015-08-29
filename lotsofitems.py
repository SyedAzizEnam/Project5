from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('postgresql+psycopg2://catalog:udacity123@localhost/itemcatalog')
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


User1 = User(name="S.Aziz Enam", email="azizenam@gmail.com",
             picture='https://lh3.googleusercontent.com/-YGk9i8a9pNw/AAAAAAAAAAI/AAAAAAAABmI/D9eB13rcE0o/photo.jpg')
session.add(User1)
session.commit()

User2 = User(name="S Enam", email="saenam@uci.edu",
             picture='https://lh5.googleusercontent.com/-KaDah_3ilp0/AAAAAAAAAAI/AAAAAAAAAAA/kRQBpgm7-fI/photo.jpg?sz=120')
session.add(User2)
session.commit()

category1 = Category(name="Clothes", user_id = 1)

session.add(category1)
session.commit()

item1 = Item(name="Dress Shirt", 
       description= "Men's Non-Iron Regular Fit Striped Dress Shirt Blue",
       price="29.99",
       image="http://scene7.targetimg1.com/is/image/Target/17016591?wid=243&qlt=85&fmt=pjpeg",
       category_id=1,
       user_id=1)
session.add(item1)
session.commit()

item2 = Item(name="Pants", 
       description= "Haggar H26 Men's Straight Fit Original Chino Pants",
       price="23.99",
       image="http://scene7.targetimg1.com/is/image/Target/15341766?wid=138&qlt=85&fmt=pjpeg",
       category_id=1,
       user_id=1)
session.add(item2)
session.commit()

item3 = Item(name="Shoes", 
       description= "Men's Ethan Chukka Boots - Brown",
       price="49.99",
       image="http://scene7.targetimg1.com/is/image/Target/21451476?wid=243&qlt=85&fmt=pjpeg",
       category_id=1,
       user_id=1)
session.add(item3)
session.commit()

category2 = Category(name="Electronics", user_id = 1)

session.add(category2)
session.commit()

item4 = Item(name="Phone", 
       description= "iPhone 6",
       price="400.00",
       image="http://scene7.targetimg1.com/is/image/Target/16483645?wid=138&qlt=85&fmt=pjpeg",
       category_id=2,
       user_id=1)
session.add(item4)
session.commit()

item5 = Item(name="Computer", 
       description= "iBuyPower Gamer Power PC (TG731) with Intel Core i",
       price="669.99",
       image="http://scene7.targetimg1.com/is/image/Target/14701254?wid=138&qlt=85&fmt=pjpeg",
       category_id=2,
       user_id=1)
session.add(item5)
session.commit()

item6 = Item(name="Camera", 
       description= "Nikon D3200 24.2MP Digital SLR Camera with 18-55mm",
       price="449.99",
       image="http://scene7.targetimg1.com/is/image/Target/14129489?wid=243&qlt=85&fmt=pjpeg",
       category_id=2,
       user_id=1)
session.add(item6)
session.commit()

category = Category(name="New Catergory", user_id = 2)

session.add(category)
session.commit()

item7 = Item(name="ITEM", 
       description= "ITEM",
       price="449.99",
       image="http://scene7.targetimg1.com/is/image/Target/14129489?wid=243&qlt=85&fmt=pjpeg",
       category_id=3,
       user_id=2)
session.add(item7)
session.commit()

print "added items!"
