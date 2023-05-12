import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.cat import Cat

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_cat(app):
    cat =  Cat(
        name="Foo",
        color="black",
        personality="sleepy"
    )
    db.session.add(cat)
    db.session.commit()
    return cat