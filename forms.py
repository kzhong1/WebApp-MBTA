from wtforms import Form, StringField, validators

class PlaceForm(Form):
    place_name = StringField('place_name', [
        validators.DataRequired("You must write a place name for querying"),
        validators.Length(min=3, max=35)
    ])