from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Task


def index(request):
    task = Task.objects.all()
    return render(request, 'index.html', {
        'task': task
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {
        'categories': categories
    })


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if color and name:
            category = Category(
                name=name,
                color=color
            )
            category.save()
    return render(request, 'add_category.html')


def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if color and name:
            category.name = name
            category.color = color
            category.save()
    return render(request, 'edit_category.html', {
        'category': category
    })


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories-list')


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


def add_tasks(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'add_task.html', {
            'categories': categories
        })
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        if name and description and category_id:
            task = Task(
                name=name,
                description=description,
                category_id=category_id
                )
            task.save()
            return redirect('tasks-list')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasks-list')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'edit_task.html', {
            'task': task,
            'categories': categories
        })
    else:
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        if name and description and category_id:
            task.name = name
            task.description = description
            task.category_id = category_id
            task.save()
            return redirect('tasks-list')
