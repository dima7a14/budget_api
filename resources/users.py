"""
This is the users resource and supports all the REST actions for the users data
"""

from flask import make_response, abort
from config import db
from models.User import User, UserSchema


def read_all():
    """
    This function responds to a request for /api/users
    with the complete lists of users

    :return: list of users
    """
    users = User.query.order_by(User.created_at).all()

    # Serialize the data for the response
    user_schema = UserSchema(many=True)
    data = user_schema.dump(users)

    return data


def read_one(id):
    """
    This function responds to a request for /api/users/{id}
    with one matching user from users

    :param id:  Id of user to find
    :return:    user matching id
    """
    user = User.query.filter(User.id == id).one_or_none()

    if user is None:
        return abort(404, f"User not found for id: {id}")

    user_schema = UserSchema()
    data = user_schema.dump(user)

    return data


def create(data):
    """
    This function creates a new user in the users structure
    based on the passed parameters in user data

    :param data:    user data to create in users structure
    :return:        201 on success, 406 on user exists
    """
    email = data.get("email")

    existing_user = User.query.filter(User.email == email).one_or_none()

    if existing_user is not None:
        return abort(409, f"User with {email} exists alread")

    schema = UserSchema()
    new_user = schema.load(data, session=db.session)

    db.session.add(new_user)
    db.session.commit()

    result = schema.dump(new_user)

    return result, 201


def update(id, data):
    """
    This function updates an existing user in the users structure
    :param id:      Id of the user to update
    :param data:    user data to update
    :return:        updated user structure
    """
    user_to_update = User.query.filter(User.id == id).one_or_none()

    if user_to_update is None:
        return abort(404, f"User not found for id: {id}")

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    existing_user = (
        User.query.filter(User.first_name == first_name)
        .filter(User.last_name == last_name)
        .one_or_none()
    )

    if existing_user is not None and existing_user.id != id:
        return abort(409, f"User {first_name} {last_name} exists already")

    schema = UserSchema()
    updated_user = schema.load(data, session=db.session)

    updated_user.id = user_to_update.id

    db.session.merge(updated_user)
    db.session.commit()

    result = schema.dump(updated_user)

    return result, 200


def delete(id):
    """
    This function deletes a user from the users structure

    :param id:  id of the user to delete
    :reutrn:    200 on successful delete, 404 if not found
    """
    user = User.query.filter(User.id == id).one_or_none()

    if user is None:
        return abort(404, f"User with id {id} not found")

    db.session.delete(user)
    db.session.commit()

    return make_response(f"User {id} deleted", 200)
