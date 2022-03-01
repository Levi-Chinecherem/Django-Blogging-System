from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclode = ['blog_slug', 'date_created']