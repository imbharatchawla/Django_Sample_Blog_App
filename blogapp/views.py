from django.shortcuts import render
from django.http import HttpResponse

# dummy_data
posts = [
    {
        'author': 'John Doe',
        'date': 'April, 04, 2021',
        'content_blog': 'This is a blog content',
        'content_title': 'Blog Heading'
    },
    {
        'author': 'John Doe',
        'date': 'April, 04, 2021',
        'content_blog': 'This is a blog content',
        'content_title': 'Blog Heading 2'
    }
]


# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Blog'})
