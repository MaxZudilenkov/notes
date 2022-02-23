# Собсвтенный валидатор по длине (для выведения ошибки на русском языке
from difflib import SequenceMatcher
from gettext import ngettext
import re

from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, \
    NumericPasswordValidator, UserAttributeSimilarityValidator
from django.core.exceptions import ValidationError, FieldDoesNotExist


class MinLength(MinimumLengthValidator):
    # Валидатор по длине пароля
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "Пароль должен содержать минимум %(min_length)d символов.",
                    "Пароль должен содержать минимум %(min_length)d символов.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )


class TooCommon(CommonPasswordValidator):
    # Валидатор для легкоподбираемого пароля
    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                ("Пароль слишком простой."),
                code='password_too_common',
            )


class Numeric(NumericPasswordValidator):
    # Валидатор для  пароля, состоящего только из цифр

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                ("Пароль не может состоять только из цифр."),
                code='password_entirely_numeric',
            )


class Similar(UserAttributeSimilarityValidator):
    # Валидатор для  пароля, похожего на почту или имя пользователя
    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_parts = re.split(r'\W+', value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        ("Пароль очень похож на электронную почту."),
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )
