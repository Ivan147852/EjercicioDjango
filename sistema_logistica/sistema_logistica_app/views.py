from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .system import System

# Create your views here.

def consultTracking(request):
    context = {'packages': Package.objects.all()}
    return render(request,"consultTracking.html", context)

def trackingResult(request):
    package = None

    if request.method == "POST":
        tracking = request.POST.get('package')
        package = get_object_or_404(Package, tracking=tracking)
        context = {'package':package}
        return render(request, 'trackingResult.html', context)

def formItemsList(request, formNumber):
    form = get_object_or_404(Form, formNumber=formNumber)
    formItems = FormItem.objects.filter(form=form).order_by('position')

    if request.method == 'POST':
        # Manejar la creación de un nuevo FormItem aquí
        print("package id = "+str(request.POST.get('package')))
        print("position = "+str(request.POST.get('position')))
        print("failureReason = "+str(request.POST.get('failureReason')))
        position = request.POST.get('position')
        packageId = request.POST.get('package')
        failureReason = request.POST.get('failureReason')
        print("en el principio")
        package = get_object_or_404(Package, tracking=packageId)
        form = get_object_or_404(Form, formNumber=formNumber)
        failureReason = None
        #if (failureReason != None):
        #    failureReason = get_object_or_404(FailureReason, reason=failureReason)
        # Crea el nuevo FormItem
        FormItem.objects.create(
            package= package,
            form=form,
            position=position,
            failureReason=failureReason,
        )
        # Redirige para evitar el reenvío del formulario
        context = {
            'form': form,
            'formItems': formItems,
            'packageList': System.getFreePackages(),
            'failureReasonList' : System.getFailureReasons(),
        }
        return render(request, 'formItemsList.html', context)
    
    context = {
        'form': form,
        'formItems': formItems,
        'packageList': System.getFreePackages(),
        'failureReasonList' : System.getFailureReasons(),
    }
    return render(request, 'formItemsList.html', context)
