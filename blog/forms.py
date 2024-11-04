from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'block w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500'})
        self.fields['content'].widget.attrs.update({'class': 'block w-full border border-gray-300 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500'})
        self.fields['image'].widget.attrs.update({'class': 'block w-full border border-gray-300 rounded-lg py-2 px-4 bg-gray-50 text-gray-700'})
