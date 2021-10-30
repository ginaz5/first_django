from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# global variable that entire application can access to.
# tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
def add(request):
    if request.method == "POST":
        # request.POST contains all data that user submitted 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # take data from the form
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # return exsiting data form and promopt error message to user
            return render(request,"tasks/add.html",{
                "form":form
            })
    # if user only want to get the page, return a empty form
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
