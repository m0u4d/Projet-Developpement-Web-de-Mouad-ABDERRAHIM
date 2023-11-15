from django.shortcuts import render, redirect,get_object_or_404
from .models import Equipe, Stade
from .forms import EquipeForm, StadeForm

# Create your views here.

def data_list(request):
    equipess = Equipe.objects.all()
    stades = Stade.objects.all()
    return render(request, 'playground/data_list.html', {'equipes': equipess, 'stades': stades})

def detail_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    return render(request, 'playground/detail_equipe.html', {'equipe': equipe})

def detail_stade(request, id_stade):
    stade = get_object_or_404(Stade, id_stade=id_stade)
    return render(request, 'playground/detail_stade.html', {'stade': stade})

def create_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST,  request.FILES)
        if form.is_valid():
            equipe = form.save()
            return redirect('detail_equipe', id_equipe=equipe.id_equipe)  
    else:
        form = EquipeForm()

    return render(request, 'playground/create_equipe.html', {'form': form})

def create_stade(request):
    if request.method == 'POST':
        form = StadeForm(request.POST, request.FILES)
        if form.is_valid():
            stade = form.save()
            return redirect('detail_stade', id_stade=stade.id_stade) 
    else:
        form = StadeForm()

    return render(request, 'playground/create_stade.html', {'form': form})

def delete_stade(request, id_stade):
    stade = get_object_or_404(Stade, id_stade=id_stade)
    stade.delete()
    return redirect('data_list')

def delete_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    equipe.delete()
    return redirect('data_list')

def modify_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('detail_equipe', id_equipe=id_equipe)
    else:
        form = EquipeForm(instance=equipe)
    
    return render(request, 'playground/modify_equipe.html', {'form': form, 'equipe': equipe})


def modify_stade(request, id_stade):
    stade = get_object_or_404(Stade, id_stade=id_stade)
    if request.method == 'POST':
        form = StadeForm(request.POST, request.FILES, instance=stade)
        if form.is_valid():
            form.save()
            return redirect('detail_stade', id_stade=id_stade)  
    else:
        form = StadeForm(instance=stade)

    return render(request, 'playground/modify_stade.html', {'form': form})