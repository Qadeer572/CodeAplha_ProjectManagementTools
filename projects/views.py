from django.shortcuts import render
from django.db.models import Avg
from register.models import Project
from projects.models import Task,Message,Comment
from projects.forms import TaskRegistrationForm
from projects.forms import ProjectRegistrationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)
# views.py
 
@login_required
def add_comment(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, assign=request.user)
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(task=task, text=comment_text,user=request.user)
    return redirect(f'/projects/tasks/?task_id={task_id}')

@login_required
def send_message(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, assign=request.user)
        message = request.POST.get('message')
        if message:
            Message.objects.create(task=task, sender=request.user, content=message)

        # Save or send the message — implement as needed
        print(f"Message sent: {message}")  # for now, just print or log it
    return redirect(f'/projects/tasks/?task_id={task_id}')

def tasks(request):
    if not request.user.is_authenticated:
        return redirect('core:login')
    all_tasks = Task.objects.all()
    tasks = all_tasks.filter(assign=request.user)

    selected_task = None
    task_id = request.GET.get('task_id')
    messages = Message.objects.all()
    comments = Comment.objects.all()
    task_messages = []
    task_comments = []
    if task_id:
        selected_task = get_object_or_404(Task, id=task_id, assign=request.user)
        task_messages=messages.filter(task=selected_task)
        task_comments=comments.filter(task=selected_task)


    context = {
        'tasks': tasks,
        'selected_task': selected_task,
        'comments': task_comments,
        'messages': task_messages,
    }
    return render(request, 'projects/task_message.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_project.html', context)