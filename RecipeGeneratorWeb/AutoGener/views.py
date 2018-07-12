from django.shortcuts import render, HttpResponse
from .forms import IngredientForm
# Create your views here.
def index(request):
    return render(request, 'AutoGener/home.html')


def get_ingredient(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IngredientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IngredientForm()

    return render(request, 'AutoGener/ingredientform.html', {'form': form})
