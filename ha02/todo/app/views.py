from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    c = {'todos': Todo.objects.all()}
    return render(request, 'index.html', c)


def about(request):
    return render(request, 'about.html')


def add(request):
    todo = Todo()
    todo.text = ""
    todo.date = ""
    todo.percent = 0
    todo.save()
    return render(request, 'edit.html', {'todo': todo})


def edit(request, todo_id):
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
        return HttpResponse('not valid, {}'.format(request.POST))
    else:
        return HttpResponse('not POST')


def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return HttpResponseRedirect('/')
