"""Name hold a name choice for a Request
"""
from api import db, ma

class Name(db.Model):
    __tablename__ = 'names'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024))
    state = db.Column(db.String(15), default='DRAFT')
    choice = db.Column(db.Integer)
    designation = db.Column(db.String(50), default='DRAFT')
    consumptionDate = db.Column('consumption_date', db.DateTime)
    remoteNameId = db.Column('remote_name_id', db.BigInteger)

    nrId = db.Column('nr_id', db.Integer, db.ForeignKey('requests.id'))
    # nameRequest = db.relationship('Request')

    NOT_EXAMINED = 'NE'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'


    def as_dict(self):
        return {"name": self.name, "choice": self.choice, "state": self.state, "consumptionDate": self.consumptionDate }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class NameSchema(ma.ModelSchema):
    class Meta:
        model = Name
        # fields = ('choice', 'name', 'state')