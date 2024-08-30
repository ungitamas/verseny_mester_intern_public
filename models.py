from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    Migrate(app, db)


class Event(db.Model):

    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    sport_type = db.Column(db.String(50), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    num_of_groups = db.Column(db.Integer)
    is_ended = db.Column(db.Boolean, default=False)
    teams = db.relationship('Team', backref='event',
                            cascade="all, delete-orphan")
    groups = db.relationship('Group', backref='event',
                             cascade="all, delete-orphan")
    matches = db.relationship('Match', backref='event',
                              cascade="all, delete-orphan")

    def __init__(self, name, date, sport_type, event_type, num_of_groups, is_ended):
        self.name = name
        self.date = date
        self.sport_type = sport_type
        self.event_type = event_type
        self.num_of_groups = num_of_groups
        self.is_ended = is_ended

    def __repr__(self):
        return f"Esemény: {self.name}, {self.date} sport: {self.sport_type} ({self.event_type}) csoportok száma: {self.num_of_groups}"


class Team(db.Model):

    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)
    group_id = db.Column(db.Integer)

    def __init__(self, name, event_id, group_id):
        self.name = name
        self.event_id = event_id
        self.group_id = group_id

    def __repr__(self):
        return f"Team: {self.name}, Event ID: {self.event_id} group id {self.group_id}"


class Group(db.Model):

    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)

    def __init__(self, name, event_id):
        self.name = name
        self.event_id = event_id

    def __repr__(self):
        return f"Csoport jele: {self.name} esemény id: {self.event_id}"


class Match(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)
    team1_score = db.Column(db.Integer)
    team2_score = db.Column(db.Integer)
    team1_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team2_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey(
        'groups.id'))
    team1 = db.relationship('Team', foreign_keys=[team1_id])
    team2 = db.relationship('Team', foreign_keys=[team2_id])

    def __init__(self, event_id, team1_score, team2_score, team1_id, team2_id, group_id):
        self.event_id = event_id
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.group_id = group_id

    def __repr__(self):
        return (f"A {self.id}. számú mérkőzés eredménye: "
                f"{self.team1_id} ({self.team1_score}) - "
                f"{self.team2_id} ({self.team2_score})")
