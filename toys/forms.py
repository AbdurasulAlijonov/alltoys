from django.forms import ModelForm
from .models import Toy, Employee


class toyForm(ModelForm):
    class Meta:
        model = Toy
        fields = ('name','user','description','tags')

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('company','first_name','last_name','email','salary')