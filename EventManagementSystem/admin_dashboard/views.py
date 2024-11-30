from django.shortcuts import render
from .models import Membership, Transaction

def admin_dashboard(request):
    memberships = Membership.objects.all()
    transactions = Transaction.objects.all()
    return render(request, 'admin_dashboard/dashboard.html', {'memberships': memberships, 'transactions': transactions})