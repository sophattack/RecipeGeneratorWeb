from django.shortcuts import render, redirect
from .forms import DishForm, IngredientForm
from .models import CanDo, CanGet
import random
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'AutoGener/home.html')



def get_dish(request):
    form = DishForm()
    canDolist = CanDo.objects.all()
    message = ''
    if request.method == 'POST':
        form = DishForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check notice
            new_dish_name = request.POST.get('name')
            dish_ingredient_str = request.POST.get('dish_ingredient')
            dish_ingredient_list = dish_ingredient_str.split('，')
            try:
                dish = CanDo.objects.get(name=new_dish_name)
                # 菜已经存在, 但没有再次输入食材
                if not dish_ingredient_str:
                    message = '你已经有这道菜了,请重新输入'
                    context = {'canDolist': canDolist, 'form': form, 'message': message}
                    return render(request, 'AutoGener/dishform.html', context)
                # 菜已经存在，再次输入了食材，删除原食材重建
                else:
                    dish.delete()
                    raise ObjectDoesNotExist

            # 菜不存在
            except ObjectDoesNotExist:
                # 新建菜
                dish = form.save(commit=False)
                dish.save()
                message = '成功添加'
            if dish_ingredient_str:
                for ingredient in dish_ingredient_list:
                    try:
                        ingre = CanGet.objects.get(name=ingredient)
                        dish.ingre.add(ingre)
                    except ObjectDoesNotExist:
                        message = "请先添加%s, 再回来添加" % ingredient
            # 菜存在，但是没有食材
            else:
                message = '请输入食材'

    context = {'canDolist': canDolist, 'form': form, 'message': message}
    return render(request, 'AutoGener/dishform.html', context)


def get_ingredient(request):
    form = IngredientForm()
    ingredientlist = CanGet.objects.all()
    duplicate = ''
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check duplicate
            new_inge_name = request.POST.get('name')
            dish = CanGet.objects.filter(name=new_inge_name)
            if dish.exists():
                duplicate = '已有该食材，请重新输入'
            else:
                new_inge = form.save(commit=False)
                new_inge.save()
                duplicate = '添加成功'


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
