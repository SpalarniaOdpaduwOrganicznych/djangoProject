from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm
from django.contrib.auth import logout 

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request): 
    return render(request, 'core/contact.html')



def rules(request): 
    return render(request, 'core/rules.html')

def privacy_policy(request): 
    return render(request, 'core/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    }) 

