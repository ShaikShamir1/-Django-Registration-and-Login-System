from django import forms
from app1.models import RegistForm

class RegForm(forms.ModelForm):
    class Meta:
        model=RegistForm
        fields=['username','first_name','last_name','mob','email','password']

    def clean(self):
        user=self.cleaned_data['username']
        if len(user)<6 and user[0].is_lower():
            raise ValueError('Username should be Captilize and more than 6 characters.')
        mob=self.cleaned_data['mob']
        if len(str(mob))!=10 and str(mob)[0] not in ['6','7','8','9']:
            raise ValueError('mobile number should stats with 6, 7, 8, 9 and at least 10 digits.')