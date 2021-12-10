from django.shortcuts import render,redirect
from .models import profile
from .forms import ProfileForm
from django.views.generic import ListView,DetailView

def index(request):
    return render(request,'index.html')


def follow_unfollow_profile(request):
    if request.method=="POST":
        my_profile=profile.objects.get(user=request.user)
        pk= request.POST.get('profile_pk')
        obj = profile.objects.get(pk=pk)
        # newly added 
        if my_profile.user in obj.followers.all():
            obj.followers.remove(my_profile.user)
        else:
            obj.followers.add(my_profile.user)


        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profilelistView')


# def my_profile_view(request):
#     print(request.user)
#     obj= profile.objects.get(user=request.user)
#     form= ProfileForm()
#     context={

#         'obj': obj,
#         'form': form,

#     }
    
#     return render(request,'myprofile.html',context)

# ---------new--------------
class ProfileListView(ListView): 
    model =profile
    template_name = 'main.html'
    context_object_name='profiles'
    def get_queryset(self):
        return profile.objects.all().exclude(user=self.request.user)
    

class ProfileDetailView(DetailView):
    model=profile
    template_name ='detail.html'
    # getting object of the current selected profile
    def get_object(self, **kwargs):
        pk =self.kwargs.get('pk')
        # getting the profile
        view_profile = profile.objects.get(pk=pk)
        return view_profile

    #  function for passing some variables to tamplate
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # getting profiles and passing them
        # selected profikle
        view_profile = self.get_object()
        # my profile 
        my_profile= profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow=True
        else:
            follow=False

        context["follow"]=follow
        return context

    




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
