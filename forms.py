from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, DateField, HiddenField
from wtforms.validators import DataRequired, InputRequired
from models import Event


class AddForm(FlaskForm):
    name = StringField('Event Name:', validators=[DataRequired()])
    date = DateField('Event Date:', format='%Y-%m-%d',
                     validators=[DataRequired()])
    sport_type = SelectField('Sportág:', choices=[('', '-Válassz egy sportágat-'),
                             ('football', 'Labdarúgás'),
                             ('basketball', 'Kosárlabda'),
                             ('handball', 'Kézilabda'),
                             ('volleyball', ('Röplabda'))])
    event_type = SelectField('Esemény típusa:', choices=[('', '-Válassz lebonyolítást-'), ('round_robin', 'Körmérkőzéses rendszer'),
                                                         ('knockout',
                                                          'Egyenes kieséses rendszer'),
                                                         ('group_knockout', 'Csoportkörös majd egyeneskieséses rendszer')],
                             validators=[DataRequired()])
    num_of_groups = SelectField('Csoportok száma:', choices=[('', '-'),
                                (2, '2 csoport'), (4, '4 csoport'), (8, '8 csoport')])
    submit = SubmitField('Esemény létrehozása')


class AddTeamForm(FlaskForm):
    name = StringField('Csapatnév:', validators=[DataRequired()])
    event_id = IntegerField('event_id', validators=[
                            DataRequired()], render_kw={'readonly': True})
    submit = SubmitField('Csapat hozzáadása')


class AssignTeamForm(FlaskForm):
    team = SelectField('Válassz egy csapatot', coerce=int,
                       validators=[DataRequired()])
    group = SelectField('Válassz egy csoportot', coerce=int,
                        validators=[DataRequired()])
    submit = SubmitField('Hozzárendelés')


class MatchResultForm(FlaskForm):
    match_id = HiddenField('Match ID')
    team1_score = IntegerField('Hazai:', validators=[InputRequired()])
    team2_score = IntegerField('Vendég', validators=[InputRequired()])
    submit = SubmitField('Submit')
