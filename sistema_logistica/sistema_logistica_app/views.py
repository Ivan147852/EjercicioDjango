from django.shortcuts import render, get_object_or_404
from .models import *
from .enums import StatesEnum

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
    states = StatesEnum.getStatesEnumChoices()
    if request.method == 'POST':
        position = request.POST.get('position')
        packageId = request.POST.get('package')
        failureReason = request.POST.get('failureReason')
        package = get_object_or_404(Package, tracking=packageId)
        form = get_object_or_404(Form, formNumber=formNumber)
        failureReason = None
        try:
            FormItem.objects.create(
                package= package,
                form=form,
                position=position,
                failureReason=failureReason,
            )
        except:
            mensaje_error = "Ya existe un objeto con este valor único."
            context = {
                'form': form,
                'formItems': formItems,
                'packageList': Package.getFreePackages(),
                'failureReasonList' : FailureReason.getFailureReasons(),
                'states':states,
                'mensaje_error': mensaje_error,
            }
            return render(request, 'formItemsList.html', context)
    
    context = {
        'form': form,
        'formItems': formItems,
        'packageList': Package.getFreePackages(),
        'failureReasonList' : FailureReason.getFailureReasons(),
        'states': states
    }
    return render(request, 'formItemsList.html', context)

def deleteFormItem(request, formNumber, formItemPosition):
    form = get_object_or_404(Form, formNumber=formNumber)
    try:
        formItem = FormItem.objects.get(form=form, position=formItemPosition)
        formItem.delete()
    except FormItem.DoesNotExist:
        pass

    formItems = FormItem.objects.filter(form=form).order_by('position')
    states = StatesEnum.getStatesEnumChoices()

    context = {
            'form': form,
            'formItems': formItems,
            'packageList': Package.getFreePackages(),
            'failureReasonList' : FailureReason.getFailureReasons(),
            'states': states
            }

    return render(request, 'formItemsList.html', context)

def changePackageState(request, formNumber):
    form = get_object_or_404(Form, formNumber=formNumber)
    formItems = FormItem.objects.filter(form=form).order_by('position')

    for f in formItems:
        f.package.state = request.POST['newState']
        f.package.save()

    states = StatesEnum.getStatesEnumChoices()
    context = {
            'form': form,
            'formItems': formItems,
            'packageList': Package.getFreePackages(),
            'failureReasonList' : FailureReason.getFailureReasons(),
            'states': states
    }

    return render(request, 'formItemsList.html', context)