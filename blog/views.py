from django.shortcuts import render

posts = [
    {
        'author': 'Amish',
        'title': 'Blog post 1',
        'content': 'My first post',
        'date_posted': 'April 16, 2024'
    },
    {
        'author': 'CoreyMs',
        'title': 'Blog post 2',
        'content': 'My first post',
        'date_posted': 'April 24, 2024'
    },
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
