from app import create_app, db
from app.models.cat import Cat

my_app = create_app()
with my_app.app_context():
    db.session.add(Cat(name="Pepper", color="black", personality="spicy"))
    db.session.add(Cat(name="Constance", color="black", personality="cold and distant"))
    db.session.add(Cat(name="Rhubarb", color="white & gray", personality="extra spicy"))
    db.session.add(Cat(name="Kiki", color="gray", personality="tender and sweet"))
    db.session.commit()