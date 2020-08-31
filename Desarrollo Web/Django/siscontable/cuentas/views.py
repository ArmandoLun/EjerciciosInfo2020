import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404
from cuentas.models import Cuenta, Movimiento

# Create your views here.
def hoy(request):
	ahora = datetime.datetime.now()
	html = '<html><body> <h1>{0}.</h1> </body></html>'.format(ahora)
	return HttpResponse(html)

def cuentas(request):
	cuentas = Cuenta.objects.all()
	total = Cuenta.objects.all().count()
	return render(request, 'cuentas2.html',{'cuentas':cuentas,'total':total})

def cuentasIndiv(request, id):
	try:
		c = Cuenta.objects.get(pk=id)
	except Cuenta.DoesNotExist:
		raise Http404("Error")
	return render(request, 'cuentaDinamica.html',{'cuenta':c,'movimientos':Movimiento.ultimos(c.id)} )
