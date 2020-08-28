import datetime
from django.shortcuts import render
from django.http import HttpResponse
from cuentas.models import Cuenta
# Create your views here.
def hoy(request):
	ahora = datetime.datetime.now()
	html = '<html><body> <h1>{0}.</h1> </body></html>'.format(ahora)
	return HttpResponse(html)

def cuentas(request):
	cuentas = Cuenta.objects.all()
	total = Cuenta.objects.all().count()
	return render(request, 'cuentas2.html',{'cuentas':cuentas,'total':total})	
