from django.shortcuts import render, get_object_or_404
from .models import *

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