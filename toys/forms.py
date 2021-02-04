from django.forms import ModelForm
from .models import Toy

class toyForm(ModelForm):
    class Meta:
        model = Toy
        fields = ('name','user','description','tags')