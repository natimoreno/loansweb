# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404

from loans.forms import ClientForm
from loans.models import Client


def index(request):
    """Index view. """
    return render(request, 'index.html')


def thank(request):
    """Thanl view."""
    return render(request, 'thank.html')


def newloan(request):
    """New loan view.

    Args:
        request: request
    """
    context = RequestContext(request)
    error = ""

    if request.method == 'POST':
        form = ClientForm(data=request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('thank')
        else:
            error = form.errors
    else:
        form = ClientForm()
    return render(
        request,
        'newloan.html',
        {'form': form, 'message': error }
    )


@login_required(login_url='login')
def editloan(request, client_id):
    """Edit loan view.

    Args:
        request: request
        client_id: client id
    """

    error = ""
    obj = get_object_or_404(Client, pk=client_id)
    form = ClientForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj.save()
            return redirect('thank')
        else:
            error = form.errors
    return render(
        request,
        'editloan.html',
        {'form': form, 'message': error, 'client': obj}
    )


@login_required(login_url='login')
def loans(request):
    """Loans view. """
    latest_client_list = Client.objects.order_by('-id')[:5]
    context = {'latest_client_list': latest_client_list}
    return render(request, 'loans.html', context)
