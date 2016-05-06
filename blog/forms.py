from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            # 'title': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'text': forms.Textarea(attrs={'class': 'mdl-textfield__input', 'rows': '5'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
