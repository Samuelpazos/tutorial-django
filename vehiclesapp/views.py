from django.shortcuts import render, redirect, get_object_or_404
from .models import vehiculo
from .forms import vehiculoForm

# Create your views here.

def list_vehiculos(request):
    vehiculos = vehiculo.objects.all()
    return render(request, 'list_view.html', {'vehiculos': vehiculos})

def create_vehiculo(request):
    if request.method == 'POST':
        form = vehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = vehiculoForm()
    return render(request, 'create_view.html', {'form': form})

def update_vehiculo(request, id):
    vehiculo_obj = get_object_or_404(vehiculo, id=id)
    if request.method == 'POST':
        form = vehiculoForm(request.POST, instance=vehiculo_obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = vehiculoForm(instance=vehiculo_obj)
    return render(request, 'update_view.html', {'form': form})

def delete_vehiculo(request, id):
    vehiculo_obj = get_object_or_404(vehiculo, id=id)
    vehiculo_obj.delete()
    return redirect('/')
