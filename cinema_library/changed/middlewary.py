class SingletonLog(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonLog, cls).__new__(cls)
        return cls.instance


class LoggedInUser:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggedInUser, cls).__new__(cls)
        return cls.instance

    user = None
    request = None

    def set_data(self, request):
        self.request = id(request)
        if request.user.is_authenticated:
            self.user = request.user

    @property
    def current_user(self):
        return self.user

    @property
    def have_user(self):
        return self.user is not None


class LoggedChangedMiddlewary(object):
    def __init__(self, get_response):
        self.get_responce = get_response

    def __call__(self, request):
        logged_in_user = LoggedInUser()
        logged_in_user.set_data(request)
        responce = self.get_responce(request)
        return responce
