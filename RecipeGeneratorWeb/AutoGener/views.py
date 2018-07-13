from django.shortcuts import render, redirect
from .forms import DishForm, IngredientForm
from .models import CanDo, CanGet

# Create your views here.
def index(request):
    return render(request, 'AutoGener/home.html')


def get_dish(request):
    form = DishForm()
    canDolist = CanDo.objects.all()
    duplicate = False
    if request.method == 'POST':
        form = DishForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check duplicate
            new_dish_name = request.POST.get('name')
            dish = CanDo.objects.filter(name=new_dish_name)
            if dish.exists():
                duplicate = True
            else:
                new_dish = form.save(commit=False)
                new_dish.save()
            # context = {'canDolist': canDolist, 'form': form, 'duplicate': duplicate}
            # return render(request, 'AutoGener/dishform.html', context)
    context = {'canDolist': canDolist, 'form': form, 'duplicate': duplicate}
    return render(request, 'AutoGener/dishform.html', context)


def get_ingredient(request):
    form = IngredientForm()
    ingredientlist = CanGet.objects.all()
    duplicate = False
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check duplicate
            new_inge_name = request.POST.get('name')
            dish = CanGet.objects.filter(name=new_inge_name)
            if dish.exists():
                duplicate = True
            else:
                new_inge = form.save(commit=False)
                new_inge.save()
    context = {'ingredientlist': ingredientlist, 'form': form, 'duplicate': duplicate}
    return render(request, 'AutoGener/ingredientform.html', context)
