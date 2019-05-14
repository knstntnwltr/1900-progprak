from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    # get all todos and render as context
    return render(request, 'index.html', {'todos': Todo.objects.all()})


def about(request):
    # simply show about sceen
    return render(request, 'about.html')


def add(request):
    # create new object
    todo = Todo()
    # fill it with nothing
    todo.text, todo.date, todo.percent = '', '', 0
    todo.save()
    # render teh site with empty form
    return render(request, 'edit.html', {'todo': todo})


def edit(request, todo_id):
    # get object and give as context
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'edit.html', {'todo': todo})


def update(request, todo_id):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.get(pk=todo_id)
            todo.text = form.cleaned_data.get('text')
            todo.date = form.cleaned_data.get('date')
            todo.percent = form.cleaned_data.get('percent')
            todo.save()
            return HttpResponseRedirect('/')
        return HttpResponse('not valid')
    else:
        return HttpResponse('not POST')


def delete(request, todo_id):
    # get object, delete
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    # redirect to home
    return HttpResponseRedirect('/')
