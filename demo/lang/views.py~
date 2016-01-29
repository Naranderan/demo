from django.shortcuts import render
from django.http import HttpResponse

from .models import Language

# Create your views here.

#def list_language(request):
#	return render(request, 'lang/list_lang.html', {"languages": Language.objects.all()})
	
def add_language(request):
	newlang = Language(name=request.POST.get('lang_name'))
	newlang.save()
	print "Testing Saving the Language"
	return render(request, 'lang/list_lang.html', {"languages": Language.objects.all()})
#	return render(request, 'lang/add_form.html', {})
	
#def add_form(request):
#	return render(request, 'lang/add_form.html', {})
	
def index(request):
    return render(request, 'lang/add_form.html', {})
    
    
