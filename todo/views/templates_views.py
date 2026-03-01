from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from ..models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/todo.html", {"todos": todos})


class TodoListViewCBV(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, "todo/todo.html", {"todos": todos})


class TodoListGenericView(ListView):
    model = Todo
    template_name = "todo/todo.html"  # 기본: todo_list.html
    context_object_name = "todos"  # 기본: object_list


# 목록 조회
class TodoListView(ListView):
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    ordering = ["-created_at"]


# 생성
class TodoCreateView(CreateView):
    model = Todo
    fields = ["name", "description", "complete", "exp"]
    template_name = "todo/create.html"
    success_url = reverse_lazy("todo:list")


# 상세보기
class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = "todo"


# 수정하기
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["name", "description", "complete", "exp"]
    template_name = "todo/update.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo:list")
