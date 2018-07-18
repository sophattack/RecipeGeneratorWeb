from django.shortcuts import render, redirect
from .forms import DishForm, IngredientForm
from .models import CanDo, CanGet
import random
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
                dish_ingredient_str = request.POST.get('dish_ingredient')
                dish_ingredient_list = dish_ingredient_str.split(',')
                for ingredient in dish_ingredient_list:
                    ingre = CanGet.objects.get(name=ingredient)
                    new_dish.ingre.add(ingre)

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

# def delete_ingredient(request, name):



def get_scehdele(request):
    random_dish = []
    message = ''
    if request.method == 'POST':
        need = request.POST.get('numNeed')
        count = CanDo.objects.all().count()
        if not need.isdigit():
            message = '请输入数字'
        else:
            if count < int(need):
                message = '你的菜不足%s道哦' % need
                random_dish = CanDo.objects.all()
            if count == int(need):
                random_dish = CanDo.objects.all()
            elif count > int(need):
                random_dish = CanDo.objects.order_by('?')[:int(need)]
    return render(request, 'AutoGener/schedule.html', {'random_dish': random_dish, "message": message})
