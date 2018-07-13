from django.shortcuts import render, redirect
from .forms import DishForm
from .models import CanDo

# Create your views here.
def index(request):
    return render(request, 'AutoGener/home.html')


def get_dish(request):
    form = DishForm()
    if request.method == 'POST':
        form = DishForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_dish = form.save(commit=False)
            new_dish.save()
            # redirect to a new URL:
            return redirect('/dish')
    canDolist = CanDo.objects.all()
    context = {'canDolist': canDolist, 'form': form}
    return render(request, 'AutoGener/dishform.html', context)

