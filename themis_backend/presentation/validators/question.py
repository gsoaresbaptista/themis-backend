from cerberus import Validator

from .base import BaseValidator


class QuestionValidator(BaseValidator):
    _query_validator = Validator(
        {
            'question': {
                'type': 'string',
                'empty': False,
                'maxlength': 512,
                'required': True,
            },
            'settings': {
                'type': 'dict',
                'required': False,
                'schema': {
                    'temperature': {
                        'type': 'float',
                        'required': False,
                    }
                },
            },
        }
    )
