class YearSerializerMixin:
    def get_data_serializer_mixin(self, param):
        queryset = self.get_queryset()
        if not hasattr(queryset[0], param):
            raise Exception('Ошибка параметра')
        data = [getattr(i, param) for i in queryset]
        return data
