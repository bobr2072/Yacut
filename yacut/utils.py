from functools import wraps
from http import HTTPStatus

from flask import request

from yacut import constants as const
from yacut import db
from yacut.exceptions import APIRequestError


def save(obj):
    db.session.add(obj)
    db.session.commit()


def required_fields(fields, message=const.FIELD_IS_REQUIRED):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            data = request.get_json()
            if not data:
                raise APIRequestError(const.EMPTY_REQUEST_BODY, HTTPStatus.BAD_REQUEST)

            for field in fields:
                if field not in data or field is None:
                    raise APIRequestError(message.format(field=field), HTTPStatus.BAD_REQUEST)

            return func(*args, **kwargs)

        return wrapper

    return decorator
