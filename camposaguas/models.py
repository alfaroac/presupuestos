# -*- coding: utf-8 -*-

from django.db import models


class Vereda(models.Model):
    tip = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    hay = (
        ('si', 'si'),
        ('no', 'no'),
    )

    nombre = models.CharField(choices=hay, max_length=2, blank=True)
    tipo = models.CharField(choices=tip, max_length=15, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '%s | %s ' %(self.nombre, self.tipo)


class Rotura(models.Model):
    tip_ro = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    
    nombre = models.CharField(max_length=15)
    tipo = models.CharField(choices=tip_ro, max_length=15, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s | %s' %(self.nombre, self.tipo)


class Reposicion(models.Model):
    nom_re = (
        ('tierra', 'tierra'),
        ('asfalto', 'asfalto'),
        ('concreto', 'concreto'),
    )
    tip_rep = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    nombre = models.CharField(choices=nom_re, max_length=15, blank=True)
    tipo = models.CharField(choices=tip_rep, max_length=15, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s | %s' %(self.nombre, self.tipo)


class TipoPista(models.Model):
    rotura = models.ForeignKey(Rotura)
    reposicion = models.ForeignKey(Reposicion)
    nombre = models.CharField(max_length=40)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Tendido(models.Model):
   
    tip_ten = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(choices=tip_ten, max_length=15, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return 'nombre:%s tipo:%s' % (self.nombre, self.tipo)


class CajaMedidor(models.Model):

    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=15)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class DiametroAgua(models.Model):
    tendido = models.ForeignKey(Tendido)
    caja_medidor = models.ForeignKey(CajaMedidor)
    nombre = models.CharField(max_length=15)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Empalme(models.Model):
    tip_emp = (
        ('60', '60'),
        ('160', '160'),
        ('200', '200'),
    )
    tip_serv = (
        ('agua', 'agua'),
        ('desague', 'desague')
    )
    nombre = models.CharField(max_length=15)
    tipo_empalme = models.CharField(choices=tip_emp, max_length=3, blank=True)
    tipo_servicio_empalme = models.CharField(
        choices=tip_serv, max_length=8, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Eliminacion(models.Model):
    tip_se = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    tipo = models.CharField(choices=tip_se, max_length=15, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo


class Relleno(models.Model):

    tip_re = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    tipo = models.CharField(choices=tip_re, max_length=15, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo


class Cama(models.Model):

    tip_serc = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    tipo = models.CharField(choices=tip_serc, max_length=15, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo


class PruebaHidraulica(models.Model):

    tip_prueb = (
        ('agua', 'agua'),
        ('alcantarillado', 'alcantarillado'),
    )
    tipo = models.CharField(choices=tip_prueb, max_length=15, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo


class Excavacion(models.Model):

    tip_exc = (
        ('agua', 'agua'),
        ('desague', 'desague'),
    )
    tipo = models.CharField(choices=tip_exc, max_length=15, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo


class Agua(models.Model):
    interesado = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)
    vereda = models.ForeignKey(Vereda)
    pista = models.ForeignKey(TipoPista)
    diametro_agua = models.ForeignKey(DiametroAgua)
    empalme = models.ForeignKey(Empalme)
    eliminacion = models.ForeignKey(Eliminacion)
    relleno = models.ForeignKey(Relleno)
    cama = models.ForeignKey(Cama)
    prueba_hidraulica = models.ForeignKey(PruebaHidraulica)
    excavacion = models.ForeignKey(Excavacion)
    distancia = models.IntegerField()

    def __str__(self):
        return self.interesado
