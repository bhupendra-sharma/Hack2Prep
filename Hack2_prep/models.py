from RequestManager import db

class Actor(db.Document):
    username = db.StringField(required=True,primary_key=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)

    def to_json(self):
        return {
            "username":self.username,
            "password": self.password,
            "author":self.role
        }