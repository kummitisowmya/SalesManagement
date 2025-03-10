from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return render(request, '403.html')  # Unauthorized access
    return render(request, 'admin_dashboard.html')

@login_required
def sales_dashboard(request):
    if request.user.role != 'sales':
        return render(request, '403.html')  # Unauthorized access
    return render(request, 'sales_dashboard.html')