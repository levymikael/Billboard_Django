from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from .models import Post

# Create your views here.
@login_required
def index(request):
    latest_post_list = Post.objects.order_by('-post_publish_date')[:]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'SocialBoard/board.html', context)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def logged_out(request):
    return render(request, 'registration/logged_out.html')


@csrf_protect
def add_new_post(request):
    if request.POST:
        new_post_input = {
            "post_title": request.POST.get("title"),
            "post_content": request.POST.get("message"),
            "post_author": request.POST.get("author"),
            "post_publish_date": request.POST.get("date")
        }
        new_post = Post.objects.create(**new_post_input)
        return HttpResponseRedirect("/")
    else:
        return render(request, "SocialBoard/board.html")