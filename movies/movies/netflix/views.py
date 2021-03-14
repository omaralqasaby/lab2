from django.shortcuts import render,redirect
from .forms import movieForm
from .models import movie 
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def index(request):
    movies = movie.object.all()

    return render(request,'netfilx/index.html',{
        "movies" : movies
    })

@login_required
@permission_required('netflix.view_movie')
def show(request,id):
    movie = movie.object.get(PK=id)
    return render(request,'netfilx/show.html',{
        "movie" : movie
    })
@login_required
def create(request):
    form = movieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'netfilx/create.html',{
        "form" : form
    })


@login_required
def update(request):
    movie = movie.object.get(PK=id)
    form = movieForm(request.POST or None , request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'netfilx/edit.html',{
        "form" : form,
        "movie" : movie
    })
@login_required
def delete(request,id):
    movie = movie.object.get(PK=id)
    movie.delete()
    return redirect('index')