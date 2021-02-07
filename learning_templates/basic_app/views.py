from django.shortcuts import render

# Create your views here.
def index(request):
    dec={'text':'hi there this is text','number':100}
    return render(request,'basic_app/index.html',dec)
def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
