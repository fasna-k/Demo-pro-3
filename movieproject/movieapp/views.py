from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movie_form
from . models import Movie

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }

    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'obj':movie})

def add_movie(request):
    if request.method=='POST':
        l1 = request.POST.get('name')
        l2 = request.POST.get('description')
        l3 = request.POST.get('year')
        l4 = request.FILES['image']
        l5 = request.POST.get('director')
        l6 = request.POST.get('price')
        movie=Movie(name=l1,description=l2,year=l3,image=l4,director=l5,price=l6)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movie_form(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')

    return render(request,'delete.html')
