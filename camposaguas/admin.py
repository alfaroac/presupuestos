from django.contrib import admin
from .models import Agua, Vereda, TipoPista, DiametroAgua, Empalme, Eliminacion, Relleno, Cama, PruebaHidraulica, Excavacion, Rotura, Reposicion,Tendido, CajaMedidor
# Register your models here.
admin.site.register(Agua)
admin.site.register(Rotura)
admin.site.register(Reposicion)
admin.site.register(Vereda)
admin.site.register(TipoPista)
admin.site.register(DiametroAgua)
admin.site.register(Empalme)
admin.site.register(Eliminacion)
admin.site.register(Relleno)
admin.site.register(Cama)
admin.site.register(PruebaHidraulica)
admin.site.register(Excavacion)
admin.site.register(Tendido)
admin.site.register(CajaMedidor)