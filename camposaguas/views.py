from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from .models import Agua
from .forms import AguaForm

def index(request):
	lista=Agua.objects.all()
	numreg=lista.count()
	return render(request, 'campoaguas/aguas/aguas.html', {'lista':lista, 'cantidad':numreg})

def addAgua(request):
	if request.method=='POST':
		objform=AguaForm(request.POST)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('index'))
	else:
		objform=AguaForm()
	return render(request,'campoaguas/aguas/addAgua.html', {'form':objform})

def updAgua(request, id):
	objedit=Agua.objects.get(pk=id)
	if request.method=='POST':
		objform=AguaForm(request.POST,instance=objedit)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('index'))
	else:
		objform=AguaForm(instance=objedit)
	return render(request, 'campoaguas/aguas/updAgua.html', {'form':objform}, context_instance=RequestContext(request))

def delAgua(request, id, template_name = 'campoaguas/aguas/delAgua.html'):
	obj_delete=Agua.objects.get(pk=id)
	if request.method=='POST':
		obj_delete.delete()
		return redirect(reverse('index'))
	return render(request, template_name, {'object':obj_delete})