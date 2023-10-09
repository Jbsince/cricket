from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import profile
from . forms import playerForm

# Create your views here.
def index(request):
    pro=profile.objects.all()
    context={
        'profile_list':pro,
        'is_index_page': True
    }

    return render(request,"index.html",context)

def details(request,profile_id):
    pro = profile.objects.get(id=profile_id)
    return render(request, "details.html", {'pro': pro})

def add_player(request):
    if request.method=="POST":
        name=request.POST.get('name')
        country=request.POST.get('country')
        dob=request.POST.get('dob')
        role=request.POST.get('role')
        img=request.FILES['img']
        player=profile(name=name,country=country,dob=dob,role=role,img=img)
        player.save()
        return redirect('/')
    return render(request,"add_player.html")

def update(request,id):
    player=profile.objects.get(id=id)
    form=playerForm(request.POST or None,request.FILES,instance=player)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'player':player})
def delete(request,id):
    if request.method=='POST':
        player=profile.objects.get(id=id)
        player.delete()
        return redirect('/')
    return render(request,'delete.html')

