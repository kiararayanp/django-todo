from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.


def index(request):
    if request.method == "POST":
        my_todo = request.POST.get("my_todo")
        todo = Todo(task=my_todo)
        todo.save()
        return redirect("home")
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "todo/index.html", context)


def edit(request, pk):
    try:
        my_todo = Todo.objects.get(id=pk)
        context = {"todo": my_todo}
        if request.method == "POST":
            updated_todo = request.POST.get("my_todo")
            my_todo.task = updated_todo
            my_todo.save()
            return redirect("home")
        return render(request, "todo/edit.html", context)

    except Todo.DoesNotExist:
        return redirect("home")


def delete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect("home")
    except Todo.DoesNotExist:
        return redirect("home")


def about(request):
    return render(request, "todo/about.html")
