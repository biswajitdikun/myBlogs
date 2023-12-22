from django.shortcuts import render,HttpResponse

def home(request):
    # Add any logic or data processing you need for the home view
    context = {
        'message': 'Welcome to the home page!',
    }
    return HttpResponse('Welcome to the home page!')
    # return render(request,'index.html',context)
    # return render(request, 'blog/index.html', context)

def blog(request):
    # Add any logic or data processing you need for the home view
    context = {
        'message': 'Welcome to the blog page!',
    }
    return HttpResponse('Welcome to the blog page!')
def contact(request):
    # Add any logic or data processing you need for the home view
    context = {
        'message': 'Welcome to the contact page!',
    }
    return HttpResponse('Welcome to the contact page!')

def blogpost(request,slug):
    return HttpResponse(f'You are viewing {slug}')

