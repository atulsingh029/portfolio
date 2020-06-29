from django import forms

class MailingForm(forms.Form):
    name = forms.CharField(max_length=160,required=True,label='Name',widget=forms.TextInput(attrs={ 'size': '30',}))
    email = forms.EmailField(max_length=255,required=True,label='Email',widget=forms.EmailInput(attrs={ 'size': '30',}))
    subject = forms.CharField(max_length=512,required=True,label='Subject',widget=forms.TextInput(attrs={ 'size': '30',}))
    message = forms.CharField(max_length=1024,required=True,label='Message',widget=forms.Textarea())


class VisitorForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=160, required=True,)
    email = forms.EmailField(max_length=254, required=True,)
    subscribe = forms.BooleanField(required=False, label="Subscribe To My Newsletter ")