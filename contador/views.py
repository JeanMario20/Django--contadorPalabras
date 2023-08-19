from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
import operator as op

from .forms import formInput

# Create your views here.
def contador(request):
    if request.method == "POST":
        form = formInput(request.POST)
        input = ""
        if form.is_valid():
            input = form.cleaned_data.get("userInput")
            res = op.countOf(input, " ") + 1
            context = {"form": form, "input": input,"res":res}
            return render(request, "contador.html", context)
        else:
            form = formInput()
    return render(request, "contador.html", {"form":form})
    