from django.shortcuts import render, redirect
from .models import Review

def index(request):
    title = "MYLP"
    data = {"title": title}
    return render(request, 'index.html', data)

def post(request):
    title = "Post"
    data = {"title": title}
    return render(request, 'post.html', data)

def aboutme(request):
    title = "about"
    data = {"title": title}
    return render(request, 'about.html', data)


def feedback(request):
    title = "feedback"
    feedbacks = Review.objects.filter(verified=True).order_by('-id')
    data = {"feedbacks": feedbacks, "title": title}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('feedback')
        Review.objects.create(name=name, email=email, text=text)
        return redirect('feedback')
    return render(request, 'feedback.html', data)
