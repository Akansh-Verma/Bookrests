from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': "Hello, world",
        'variable2': "World, Hello"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")