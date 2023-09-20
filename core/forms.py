from django import forms


class ContactMeForm(forms.Form):
    name = forms.CharField(max_length=60,
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}))
    massage = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'cols': '', 'rows': ''}))
