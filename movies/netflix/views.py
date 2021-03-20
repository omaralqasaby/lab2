from django.shortcuts import render,redirect
from .forms import MovieForm,CategoryForm
from .models import Movie,Category
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission
# Create your views here.
def changePermession():
    Permission.objects.filter(codename="view_movie").update(codename="show_movie")

@login_required
def index(request):
#    if not request.is_authorized:
#        return redirect("login")
    movies=Movie.objects.all()
    return render(request,'netflix/index.html',{
        'movies':movies
    })

def create(request):
    form=MovieForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'netflix/create.html',{
        'form':form
    })
@login_required
@permission_required('netflix.vew_movie')
def show(request,id):
    movie=Movie.objects.get(pk=id)
    return render(request,'netflix/show.html',{
        'movie':movie
    })
def update(request,id):
    movie=Movie.objects.get(pk=id)
    form=MovieForm(request.POST or None ,request.FILES or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'netflix/edit.html',{
        'movie':movie,
        'form':form
    })
def delete(request,id):
    movie=Movie.objects.get(pk=id)
    movie.delete()
    return redirect('index')
