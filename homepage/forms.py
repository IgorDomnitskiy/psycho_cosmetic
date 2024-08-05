from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    issue = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.SelectDateWidget)
