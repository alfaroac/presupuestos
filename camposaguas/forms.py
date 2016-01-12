from django import forms
from .models import Agua
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets



class AguaForm(forms.ModelForm):
	class Meta:
		model=Agua
 		exclude=()
