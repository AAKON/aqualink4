from django import forms

class UploadFileForm(forms.Form):
    designation = forms.CharField(max_length=50)
    pdf = forms.FileField()