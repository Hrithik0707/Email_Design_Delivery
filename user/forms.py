from django import forms
from .models import Grps,Contacts

class CreateGroupForm(forms.ModelForm):
    class Meta:
        model= Grps
        fields = ['gname','contacts']
    def __init__(self,*args,**kwargs):
        super(CreateGroupForm,self).__init__(*args,**kwargs)
        self.fields["contacts"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["contacts"].queryset = Contacts.objects.all()