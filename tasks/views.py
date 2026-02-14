from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Project, Stage, Task, Comment
from .forms import ProjectForm, TaskForm, StageForm, CommentForm

@login_required
def dashboard(request):
    projects = Project.objects.all().annotate(
        total_tasks=Count('stages__tasks'),
        done_tasks=Count('stages__tasks', filter=Q(stages__tasks__stage__name__iexact='Done'))
    )
    for project in projects:
        project.progress = int((project.done_tasks / project.total_tasks) * 100) if project.total_tasks > 0 else 0
    return render(request, 'tasks/dashboard.html', {'projects': projects})

@login_required
def project_board(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    stages = project.stages.order_by('order')
    return render(request, 'tasks/board.html', {'project': project, 'stages': stages})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments, 'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        stage_id = request.POST.get('stage')
        if form.is_valid():
            task = form.save(commit=False)
            if stage_id:
                task.stage = Stage.objects.get(id=stage_id)
            task.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.stage.project.id
    if request.method == 'POST':
        task.delete()
        return redirect('project_board', project_id=project_id)
    return render(request, 'tasks/delete_confirm.html', {'item': task})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'tasks/create_project.html', {'form': form})

@login_required
def add_task(request, stage_id):
    stage = get_object_or_404(Stage, id=stage_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.stage = stage
            task.save()
            return redirect('project_board', project_id=stage.project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'stage': stage})

@login_required
def add_stage(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            stage = form.save(commit=False)
            stage.project = project
            stage.save()
            return redirect('project_board', project_id=project.id)
    else:
        form = StageForm()
    return render(request, 'tasks/add_stage.html', {'form': form, 'project': project})