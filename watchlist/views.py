from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import CreateWatchList, PuntuarWatchList,FormComentarios
from .models import WatchList
from django.contrib.auth.decorators import login_required



# Create your views here.
def signup(request):            
    if request.method =='GET':
        return render(request,'signup.html',{ 'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
           try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])            
                user.save
                login(request,user)
                return redirect('watchlist')                
           except:
               return render(request,'signup.html',{ 'form':UserCreationForm, "error": 'Usuario ya existe'})               
        else:
            return render(request,'signup.html',{ 'form':UserCreationForm, "error": 'Contraseñas no coinciden'})               
        
@login_required        
def watchlist(request):            
    watchlist = WatchList.objects.filter(user=request.user)    
    return render(request,'watchlist.html',{'watchlist':watchlist})

def home(request):            
    return render(request,'home.html')

@login_required
def cerrar_sesion (request):
    logout(request)
    return redirect('home')

def iniciar_sesion (request):    
    if request.method =='GET':
        return render(request,'signin.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
                return render(request,'signin.html',{'form':AuthenticationForm, "error": 'Usuario o Contraseña incorrecta'})
        else:
            login(request,user)            
            return redirect('home')          

@login_required        
def create_watchlist(request): #crear
    if request.method =='GET':
        return render(request,'create_watchlist.html',{'form':CreateWatchList})
    else:
        try: 
            form = CreateWatchList(request.POST)                                  
            new_watchlist = form.save(commit=False)
            new_watchlist.user = request.user                        
            new_watchlist.description = ''            
            new_watchlist.rate = ''
            new_watchlist.visto = False            
            new_watchlist.save()           
            return redirect('home')
        except:            
            return render(request,'create_watchlist.html',{'form':CreateWatchList, 'error':'Proveer datos correctos'})

@login_required        
def puntuar(request,elem_id):    #actualizar    
    if request.method =='GET':        
        elem = get_object_or_404(WatchList,pk=elem_id, user=request.user)
        form = PuntuarWatchList(instance=elem)
        return render(request, 'puntuar.html', {'watchlist':elem, 'form':form})
    else:
        try:
            elem = get_object_or_404(WatchList,pk=elem_id, user=request.user)
            form = PuntuarWatchList(request.POST,instance=elem)
            form.save()        
            return redirect('watchlist')
        except ValueError:
            return render(request, 'puntuar.html', {'watchlist':elem, 'form':form, 'error':"No se pudo actualizar correctametne"})

@login_required        
def enviar_mensaje(request):
    if request.method == 'GET':
        form = FormComentarios()
        return render(request,'contacto.html',{'form':FormComentarios})           
    else:
        try: 
            form = FormComentarios(request.POST)                                  
            new_comentario = form.save(commit=False) 
            new_comentario.user =  request.user
            new_comentario.save()           
            return redirect('home')
        except:            
            return render(request,'contacto.html',{'form':FormComentarios, 'error':'Proveer datos correctos'})
   
        
@login_required
def sacar_listado(request,elem_id):
    watchlist = get_object_or_404(WatchList, pk=elem_id, user=request.user)
    if request.method == 'POST':
        watchlist.delete()
        return redirect('watchlist')
    

@login_required
def agregar_listado(request):
    return render(request,'home.html')

