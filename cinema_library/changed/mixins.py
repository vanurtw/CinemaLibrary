from django.db import models


class ChangLoggableMixin(models.Model):
    _original_values = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(ChangLoggableMixin, self).__init__(*args, **kwargs)
        self._original_values = {
            field.name: getattr(self, field.name) for field in self._meta.fields if
            field.name not in ['data_create'] and hasattr(self, field.name)
        }

    def change_data(self):
        result = {}
        for key, value in self._original_values.items():
            if value != getattr(self, key):
                result[key] = getattr(self, key)
        return result
