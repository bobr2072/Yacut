import random
import string
from datetime import datetime

from yacut import constants as const
from yacut import db


class URLMap(db.Model):

    original = db.Column(db.String, nullable=False)
    short = db.Column(
        db.String(const.CUSTOM_ID_LENGTH),
        nullable=False,
        unique=True,
        index=True,
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def generate_short_id(length=const.SHORT_ID_LENGTH):

        characters = string.ascii_letters + string.digits
        random_url = ''.join(random.choice(characters) for _ in range(length))
        return random_url

    @classmethod
    def is_free_short_id(cls, short_id):
        return cls.query.filter_by(short=short_id).first() is None

    @classmethod
    def get_unique_short_id(cls, length=const.SHORT_ID_LENGTH):

        while True:

            short_id = cls.generate_short_id(length)
            if cls.is_free_short_id(short_id):
                break

        return short_id