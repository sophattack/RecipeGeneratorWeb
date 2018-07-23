from django.shortcuts import render, redirect, HttpResponse
from .forms import DishForm, IngredientForm
from .models import CanDo, CanGet, DishType
import random
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

show_dishes = []

def index(request):
    """home page"""
    return render(request, 'AutoGener/home.html')



def get_dish(request):
    """ /dish.html, deal with add new dish and redirect if there is a search. """
    form = DishForm()
    canDolist = CanDo.objects.all()
    message = ''
    detail = ''
    if request.method == 'POST':
        detail = request.POST.get('dish_wanted')
        if detail:
            return get_dish_detail(request, detail, search=True)
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
                    dish_delete(request, new_dish_name)
                    raise ObjectDoesNotExist

            # 菜不存在
            except ObjectDoesNotExist:
                # 新建菜
                dish = form.save(commit=False)
                dish.save()
                form.save_m2m()
                form = DishForm()
            if dish_ingredient_str:
                not_in_ingre = ''
                for ingredient in dish_ingredient_list:
                    try:
                        ingre = CanGet.objects.get(name=ingredient)
                        dish.ingre.add(ingre)
                    except ObjectDoesNotExist:
                        not_in_ingre += ingredient + '，'
                if not_in_ingre:
                    message = "以下食材不在食品库：%s 请先去添加食材，再添加菜品，才可计算卡路里哦" % not_in_ingre
                else:
                    message = '添加成功！'
            # 菜存在，但是没有食材
            else:
                message = '成功添加，但没有记录食材'

    context = {'canDolist': canDolist, 'form': form, 'message': message, 'show_dishes': show_dishes}
    return render(request, 'AutoGener/dishform.html', context)


def dish_list_remove(request, name):
    """ remove dish=name from right side of /dish.html """
    try:
        dish = CanDo.objects.get(name=name)
        if dish in show_dishes:
            show_dishes.remove(dish)
        return redirect('/dish/')
    except ObjectDoesNotExist:
        return redirect('/dish/')

def add_type(request):
    if request.method == 'GET':
        new_type = request.GET.get('name')
        if new_type:
            DishType(name=new_type).save()
            return redirect('/dish/')
        else:
            return HttpResponse('触发ajax')


def get_dish_detail(request, name, search=False):
    """show dish detail on right side of /dish.html"""
    form = DishForm()
    message = ''
    canDolist = CanDo.objects.all()
    realted_dish = []
    ingre_list = []
    dish = CanDo()
    try:
        dish = CanDo.objects.get(name=name)
        if dish not in show_dishes:
            show_dishes.append(dish)
        realted_dish = [dish]
        ingre_list = dish.ingre.all()
        for ingre in ingre_list:
            realted_dish += ingre.cando_set.filter(~Q(name=name)).all()
    except ObjectDoesNotExist:
        try:
            ingre = CanGet.objects.get(name=name)
            realted_dish = ingre.cando_set.all()
        except ObjectDoesNotExist:
            message = "%s不在你的菜单或食材库里" % name
    if not search:
        context = {'canDolist': canDolist, 'form': form, 'message': message, 'ingre_list': ingre_list, 'dish': dish,
                'show_dishes': show_dishes}
    else:
        context = {'canDolist': realted_dish, 'form': form, 'message': message, 'ingre_list': ingre_list, 'dish': dish,
                   'show_dishes': show_dishes}
    return render(request, 'AutoGener/dishform.html', context)


def get_ingredient(request):
    """ add new ingredient on /ingredient.html """
    form = IngredientForm(auto_id="ingre_%s")
    ingredientlist = CanGet.objects.all()
    duplicate = ''
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check duplicate
            new_inge_name = request.POST.get('name')
            try:
                ingre = CanGet.objects.get(name=new_inge_name)
                # 存在且卡路里数据相同
                if ingre.cal == int(request.POST.get('cal')):
                    duplicate = '已有该食材，请重新输入'
                else:
                    ingre.delete()
                    raise ObjectDoesNotExist
            except ObjectDoesNotExist:
                new_inge = form.save(commit=False)
                new_inge.save()
                form = IngredientForm(auto_id="ingre_%s")
                duplicate = '添加/更新你的食材卡路里数据成功'
        else:
            duplicate = '请输入正确数据'

    context = {'ingredientlist': ingredientlist, 'form': form, 'duplicate': duplicate}
    return render(request, 'AutoGener/ingredientform.html', context)


def ingre_delete(request, name):
    """delete ingre from database """
    ingre = get_object_or_404(CanGet, name=name)
    ingre.delete()
    return redirect('/ingredient/')

def dish_delete(request, name):
    """delete dish from database """
    dish = get_object_or_404(CanDo, name=name)
    if dish in show_dishes:
        show_dishes.remove(dish)
    dish.delete()
    return redirect('/dish/')

def get_scehdele(request):
    """ randomly pick # of dishes from database """
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
