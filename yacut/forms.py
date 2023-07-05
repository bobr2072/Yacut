from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, ValidationError

from yacut import constants as const
from yacut.models import URLMap


class URLMapForm(FlaskForm):

    original_link = URLField(
        'Введите ссылку',
        validators=(DataRequired(message=const.FIELD_IS_REQUIRED),
                    URL(message=const.INVALID_CUSTOM_ID))
    )

    custom_id = URLField(
        validators=(Length(max=16,),)
    )

    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if field.data and not URLMap.is_free_short_id(field.data):
            raise ValidationError(f'Имя {field.data} уже занято!')
