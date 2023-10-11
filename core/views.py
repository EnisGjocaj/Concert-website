
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegisterForm
from . forms import SignupForm

# Create your views here.
def signup(request):

	if request.method == "POST":
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/login/')
	else:
		form = SignupForm()

	return render(request, 'core/signup.html', {
		'form': form,
	})

def index(request):
    if request.method == "POST":
        form =  RegisterForm(request.POST)

        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.save()
            return redirect('core:index') 
    else:
        form = RegisterForm()

    return render(request, "core/index.html", {
        "form": form,
    })

def hotels(request):
    return render(request, "core/hotels.html")
