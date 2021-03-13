from django.shortcuts import render,redirect
from .forms import movieForm
# Create your views here.
def index(request):
    pass
def create(request):
    form = movieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'netfilx/create.html',{​​​​​
        "form" : form
    }​​​​​)

def update(request,id):
    movie = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None ,request.FILES or None,instance=movie)
    if form.is_vaild():
        form.save()

        return redirect("index")
    return render(request,"netflix/create.html",{
        'form':form
        "movie":movie
    })
def delete(request,id):
    movie=Movies.objects.get(pk=id)
    movie.delete()
    return redirect("index")
def show(request,id):
    movie=Movies.objects.get(pk=id)

    return render(request,"netflix/show.html",{
        "movies":movie
    })