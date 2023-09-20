from django import forms


class ContactMeForm(forms.Form):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    massage = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))
