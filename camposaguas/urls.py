from django.conf.urls import url

urlpatterns = [
  	url(r'^$', 'camposaguas.views.index', name='index'), 
	
	#url(r'^agua$','camposaguas.views.agua', name='agua'),
	url(r'^agua/add$','camposaguas.views.addAgua', name='addAgua'),
	url(r'^agua/upd/(?P<id>\d+)$','camposaguas.views.updAgua', name='updAgua'),
	url(r'^agua/del/(?P<id>\d+)$', 'camposaguas.views.delAgua', name='delAgua'),

	# url(r'^buscar/$', buscarPorDni.as_view(), name='buscarDni'),
	#url(r'^buscar/$', buscarPorApellidos.as_view(), name='buscarApellidos'),
	#url(r'^agua/busqueda/$', 'camposaguas.views.busqueda', name='busquedaagua'),
	#url(r'^guardarevento$', 'apps.agenda.views.guardarEvento'),
]