from datetime import datetime
from flask_bcrypt import Bcrypt
from marshmallow import fields, validate

from config import app, db, ma


bcrypt = Bcrypt(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password,
            app.config["BCRYPT_LOG_ROUNDS"]
        ).decode()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    first_name = fields.String(required=True, validate=validate.Length(1, 80))
    last_name = fields.String(required=True, validate=validate.Length(1, 80))
    password = fields.String(
        required=True,
        validate=validate.Length(
            6, 120, error="Min length for password is 6."
        ),
        load_only=True,
    )
