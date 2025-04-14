from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .storage import storage
import base64

def home(request):
    posts = storage.get_all_posts()
    return render(request, 'blog/home.html', {'posts': posts})

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = None
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            image = base64.b64encode(image_file.read()).decode('utf-8')
        
        author = request.session.get('user', 'Anonymous')
        storage.create_post(title, content, author, image)
        return redirect('home')
    
    return render(request, 'blog/create_post.html')

def post_detail(request, post_id):
    post = storage.get_post(post_id)
    if post:
        return render(request, 'blog/post_detail.html', {'post': post})
    return redirect('home')
