from django import forms


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, help_text="Input Name Here.")
    email = forms.EmailField(required=True)
    message = forms.CharField(required=False, widget=forms.Textarea)
