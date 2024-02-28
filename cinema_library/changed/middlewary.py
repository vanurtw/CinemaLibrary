class SingletonLog(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(*args, **kwargs)
        return cls.instance


class LoggedInUser(metaclass=SingletonLog):
    user = None
    request = None

    def set_data(self, request):
        self.request = request
        if self.user.is_authenticated():
            self.user = request.user

    @property
    def current_user(self):
        return self.user

    @property
    def have_user(self):
        return not self.user is None


class LoggedChangedMiddlewary(object):
    def __init__(self, get_response):
        self.get_responce = get_response

    def __call__(self, request):
        logged_in_user = LoggedInUser()
        logged_in_user.set_data(request)

        responce = self.get_responce(request)

        return responce
