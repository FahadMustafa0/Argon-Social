from django.shortcuts import render
from .models import profile
from .forms import ProfileForm
def index(request):
    return render(request,'index.html')

# def my_profile_view(request):
#     print(request.user)
#     obj= profile.objects.get(user=request.user)
#     form= ProfileForm()
#     context={

#         'obj': obj,
#         'form': form,

#     }
    
#     return render(request,'myprofile.html',context)

    
def my_profile_view(request):
    obj = profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'obj': obj,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'myprofile.html', context)
