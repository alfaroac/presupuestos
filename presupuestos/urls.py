
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^main/', include('camposaguas.urls')), 
    url(r'^cerrar/', 'django.contrib.auth.views.logout_then_login',name='logout'),
]
