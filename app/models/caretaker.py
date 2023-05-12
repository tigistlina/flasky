from app import db

class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    cats = db.relationship("Cat", back_populates="caretaker")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"]
        )