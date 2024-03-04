from .models import ChangeLog
from django.http import HttpResponse


# Create your views here.


def test(request):
    chhange = ChangeLog(model='awdwa', record_id='5')
    chhange.model = 'sssssdwadsawdawd'
    chhange.change_data()
    return HttpResponse('test')
