from django import forms
from django.forms import widgets
from .models import EmployeeRefer

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeRefer
        fields ="__all__"
        widgets= {
            'firstname' : forms.TextInput(attrs ={'class':'form-control'}),
            'lastname' : forms.TextInput(attrs ={'class':'form-control'}),
            'emailid' : forms.TextInput(attrs ={'class':'form-control'}),
            'phonenumber' : forms.TextInput(attrs ={'class':'form-control'}),
            'Description' : forms.TextInput(attrs ={'class':'form-control'}),
            'position' : forms.TextInput(attrs ={'class':'form-control'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label ="Select"

from .models import PDFFile

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ('pdf_file',)