from .db import db, environment, SCHEMA, func

class Location(db.Model):
    __tablename__='location' #does this need to be plural?

    if environment == "production":
        __table_args__= {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.name,
        }
