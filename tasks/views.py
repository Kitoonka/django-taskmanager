from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField
from .models import Task

# LIST TASKS - Sorted, Filtered, Searchable
@login_required
def task_list(request):
    priority_order = Case(
        When(priority='High', then=Value(1)),
        When(priority='Medium', then=Value(2)),
        When(priority='Low', then=Value(3)),
        output_field=IntegerField()
    )

    tasks = Task.objects.filter(user=request.user).annotate(
        priority_order=priority_order
    ).order_by('completed', 'priority_order', 'due_date', '-created')

    # --- Filtering ---
    status = request.GET.get('status')  # all / completed / incomplete
    priority_filter = request.GET.get('priority')  # High / Medium / Low
    search_query = request.GET.get('search')  # text search

    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'incomplete':
        tasks = tasks.filter(completed=False)

    if priority_filter in ['High', 'Medium', 'Low']:
        tasks = tasks.filter(priority=priority_filter)

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'status': status or 'all',
        'priority_filter': priority_filter or '',
        'search_query': search_query or ''
    })

# CREATE TASK
@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date') or None
        priority = request.POST.get('priority') or 'Medium'

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                due_date=due_date,
                priority=priority
            )
            return redirect('task_list')

    return render(request, 'tasks/task_form.html')

# UPDATE TASK
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.due_date = request.POST.get('due_date') or None
        task.priority = request.POST.get('priority') or 'Medium'
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})

# DELETE TASK
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')

# MARK COMPLETE
@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')
