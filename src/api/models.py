from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(275), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<Favorites {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# _______________________________________________________________________________________________________


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __repr__(self):
        return f"<Account {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'total': self.total
        }
# _______________________________________________________________________________________________________


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=True)
    mass = db.Column(db.Integer, unique=False, nullable=True)
    hair_color = db.Column(db.String(120), unique=False, nullable=True)
    skin_color = db.Column(db.String(120), unique=False, nullable=True)
    eye_color = db.Column(db.String(120), unique=False, nullable=True)
    birth_year = db.Column(db.Integer, unique=False, nullable=True)
    gender = db.Column(db.String(120), unique=False, nullable=True)
    homeworld = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return f"<People {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'homeworld': self.homeworld
        }
# _______________________________________________________________________________________________________


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=True)
    rotation_period = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Integer, unique=False, nullable=True)
    gravity = db.Column(db.String(120), unique=False, nullable=True)
    population = db.Column(db.Integer, unique=False, nullable=True)
    climate = db.Column(db.String(120), unique=False, nullable=True)
    terrain = db.Column(db.String(120), unique=False, nullable=True)
    surface_water = db.Column(db.Integer, unique=False, nullable=True)
    url = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return f"<Planet {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'diameter': self.diameter,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'gravity': self.gravity,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'url': self.url
        }
# _______________________________________________________________________________________________________


class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    classification = db.Column(db.String(120), unique=False, nullable=True)
    designation = db.Column(db.String(120), unique=False, nullable=True)
    average_height = db.Column(db.Integer, unique=False, nullable=True)
    skin_color = db.Column(db.String(120), unique=False, nullable=True)
    hair_color = db.Column(db.String(120), unique=False, nullable=True)
    eye_color = db.Column(db.String(120), unique=False, nullable=True)
    average_lifespan = db.Column(db.Integer, unique=False, nullable=True)
    homeworld = db.Column(db.String(120), unique=False, nullable=True)
    language = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return f"<Species {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'skin_colors': self.skin_colors,
            'hair_colors': self.hair_colors,
            'eye_colors': self.eye_colors,
            'average_lifespan': self.average_lifespan,
            'homeworld': self.homeworld,
            'language': self.language
        }
# _______________________________________________________________________________________________________


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=True)
    manufacturer = db.Column(db.String(120), unique=False, nullable=True)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=True)
    length = db.Column(db.Integer, unique=False, nullable=True)
    max_atmosphering_speed = db.Column(db.Integer, unique=False, nullable=True)
    crew = db.Column(db.Integer, unique=False, nullable=True)
    passengers = db.Column(db.Integer, unique=False, nullable=True)
    cargo_capacity = db.Column(db.Integer, unique=False, nullable=True)
    consumables = db.Column(db.String(120), unique=False, nullable=True)
    vehicle_class = db.Column(db.String(120), unique=False, nullable=True)
    pilots = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return f"<Vehicles {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_class": self.vehicle_class,
            "pilots": self.pilots,
        }
# _______________________________________________________________________________________________________


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(275), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
