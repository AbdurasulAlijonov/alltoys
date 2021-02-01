from django.forms import ModelForm
from .models import toy

class toyForm(ModelForm):
    class Meta:
        model = toy
        fields = ('name','User','description','tags')