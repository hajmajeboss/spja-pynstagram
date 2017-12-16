from django import forms
from pynstagram.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created', 'photograph']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Enter your comment here. '}),
        }


class SearchUsersForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username you would like to search.'}))


class MailUserForm(forms.Form):
    sender = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))
    mail_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))
