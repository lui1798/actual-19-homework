#from datetime import datetime, timedelta
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Log

# Create your views here.


def Testmul(request):
    s = ''
    for i in range(1, 10):
        for j in range(1, i+1):
            s += '{0}×{1}={2:<2}'.format(j, i, i*j) + '  '
        s += '\n\n'
    s = ''' <h4>{0}</h4>'''.format(s)
    pageHtml = mark_safe(s)
    return render(request, 'multiplication.html', {'pageHtml':pageHtml})

def Loganalysis(request):
    objs = Log.objects.all().order_by('-query_time')[0:4]
    return render(request, 'loganalysis.html', context={'objs': objs})
