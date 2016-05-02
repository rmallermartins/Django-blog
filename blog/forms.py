from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'text': forms.Textarea(attrs={'class': 'mdl-textfield__input', 'rows': '5'}),
        }
