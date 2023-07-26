from django.shortcuts import render,redirect
from .forms import CreerUtilisateur
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
 
def inscriptionPage(request):
 form=CreerUtilisateur() 
 if request.method=='POST': 
  form =CreerUtilisateur(request.POST)
  if form.is_valid():
   form.save()
   return redirect('connexion')
 context = {'form':form}
 return render(request,'compte/inscription.html',context)

def accesPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        user = authenticate(request, email=email, password=mot_de_passe)
        if user is not None :
            messages.error(request, "Désolé")
        else:
            messages.error(request, "Utilisateur et/ou mot de passe incorrect(s)")
            return redirect('connexion')
    return render(request, 'compte/connexion.html')

def logoutUser(request):
    logout(request)
    return redirect('/')