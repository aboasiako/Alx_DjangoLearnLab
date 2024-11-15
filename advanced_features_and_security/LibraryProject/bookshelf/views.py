from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import MyModel

@permission_required('app_name.can_view', raise_exception=True)
def view_instance(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    return render(request, 'view_template.html', {'instance': instance})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_instance(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    # Logic to handle editing
    return render(request, 'edit_template.html', {'instance': instance})
