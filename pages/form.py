from django import forms

from .models import FormDetail

class Detail_form(forms.ModelForm):
    class Meta:
        model = FormDetail
        fields = '__all__'
        # fields = [
        #     'Name',
        #     'Age',
        #     'Address'
        # ]
