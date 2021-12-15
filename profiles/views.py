from django.shortcuts import render,redirect
from requests.api import request
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from .models import profile
from .forms import ProfileForm
from django.views.generic import ListView,DetailView, detail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from .serializers import ProfileSerializer,ProfileUpdateSerializer
import json
import requests
from rest_framework.decorators import api_view
from django.contrib import messages

def index(request):
    return render(request,'index.html')

#  converted to API call so commented this

# def follow_unfollow_profile(request):
#     if request.method=="POST":
#         my_profile=profile.objects.get(user=request.user)
#         pk= request.POST.get('profile_pk')
#         obj = profile.objects.get(pk=pk)
#         # newly added 
#         if my_profile.user in obj.followers.all():
#             obj.followers.remove(my_profile.user)
#         else:
#             obj.followers.add(my_profile.user)


#         if obj.user in my_profile.following.all():
#             my_profile.following.remove(obj.user)
#         else:
#             my_profile.following.add(obj.user)
#         return redirect(request.META.get('HTTP_REFERER'))
#     return redirect('profiles:profilelistView')



# new follow unfollow thourgh API
    # posting data to api and getting the result as json response
        #post Api call
def post(request):
    if request.method=="POST":
        my_profile=profile.objects.get(user=request.user)
        pk= request.POST.get('profile_pk')
        obj = profile.objects.get(pk=pk)
        body={
            'myprofile':my_profile.user.id,
            'userobj' : obj.user.id,
        }
        result=requests.post('http://127.0.0.1:8000/postapi/',data=body)
        print("---------------------------------------")
        print(result.status_code)
        if result.status_code == 200:
            messages.success(request, 'Api call is working pefectly fine : Action Successful')
        else:
            messages.success(request, 'Api call is not working fine')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profilelistView')

# post APi method
@csrf_exempt
@api_view(['POST'])
def postapi(request):
    if request.method=="POST":
        followerid=request.POST.get('myprofile')
        followedid=request.POST.get('userobj')
        followerobj = profile.objects.get(user=followerid)
        followedobj = profile.objects.get(user=followedid)
        # print(request.POST.get())
        # following=request.POST.get('myprofile')
        # followed=request.POST.get('userobj')
        if followerobj.user in followedobj.followers.all():
            followedobj.followers.remove(followerobj.user) 
        else:
            followedobj.followers.add(followerobj.user)


        if followedobj.user in followerobj.following.all():
            followerobj.following.remove(followedobj.user)
        else:
            followerobj.following.add(followedobj.user)
        print("===============================")
        
        return (Response(status= status.HTTP_200_OK))
    else:
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)


# def my_profile_view(request):
#     print(request.user)
#     obj= profile.objects.get(user=request.user)
#     form= ProfileForm()
#     context={

#         'obj': obj,
#         'form': form,

#     }
    
#     return render(request,'myprofile.html',context)

# ---------new--------------Currently displaying data
class ProfileListView(ListView): 
    model =profile
    template_name = 'main.html'
    context_object_name='profiles'
    def get_queryset(self):
        return profile.objects.all().exclude(user=self.request.user)
       

# _-------------------new for api end point----

@api_view(['GET'])
def profile_list(request,pk):
    list = profile.objects.all().exclude(user_id=pk)   
    list_serializer =ProfileSerializer(list,many=True)
    print(list_serializer.data)
    return Response(list_serializer.data)
    # return JsonResponse(list_serializer.data, safe=False)

def fetch(request):
   pk=request.user.id
   res=requests.get('http://127.0.0.1:8000/profiletlist/'+str(pk)+'/')
   datastr = json.loads(res.text)
#    print(datastr)
#    datastr=json.dumps(data)
   print(type(datastr))
   context = {
       'strdata': datastr,
   }
   return render(request,'jsonrenderer.html',context)
       




# getting the detailed view of selected profile
# class ProfileDetailView(DetailView):
#     model=profile
#     template_name ='detail.html'
#     # getting object of the current selected profile
#     def get_object(self, **kwargs):
#         pk =self.kwargs.get('pk')
#         # getting the profile
#         view_profile = profile.objects.get(pk=pk)
#         return view_profile

#     #  function for passing some variables to tamplate
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # getting profiles and passing them
#         # selected profikle
#         view_profile = self.get_object()
#         # my profile 
#         my_profile= profile.objects.get(user=self.request.user)
#         if view_profile.user in my_profile.following.all():
#             follow=True
#         else:
#             follow=False

#         context["follow"]=follow
#         return context

    
# profile detail view following or not check(to show button differently)
    # api call

def ProfileDetailView(request, pk):
    data={

        'viewprofileid' :  pk,
        'myprofileid'   : request.user.id
    }
    # check if already follow or not
    result=requests.get('http://127.0.0.1:8000/detailapi/',params=data)
    result = json.loads(result.text)

    
    view_profile = profile.objects.get(pk=pk)
    
    context={
        'follow': result['follow'],
        'object' : view_profile
    }
    
    return render(request,'detail.html',context)
    


# profile detail view api method
@api_view(['GET'])
def DetailProfileApi(request):
    view_profile = profile.objects.get(pk=request.GET.get('viewprofileid'))
    my_profile= profile.objects.get(user=request.GET.get('myprofileid'))

    if view_profile.user in my_profile.following.all():
            follow={'follow': True}
    else:
            follow={'follow': False}
    return Response(follow)







# def my_profile_view(request):
#     obj = profile.objects.get(user=request.user)
#     form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
#     confirm = False

#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             confirm = True

#     context = {
#         'obj': obj,
#         'form': form,
#         'confirm': confirm,
#     }

#     return render(request, 'myprofile.html', context)

# my_profile_view Api call
@csrf_exempt
def my_profile_api(request):
    profile_id=request.user.id
    data={
        'id':profile_id
    }
    res=requests.get('http://127.0.0.1:8000/profileviewapi/', data)
    result=json.loads(res.text)
    print(type(result))
    serialzer=ProfileSerializer(result["obj"])
    result["serializer"]=serialzer
    
#     context = {
#        'strdata':result, # result is a list of dictionary
#    }
    return render(request, 'myprofile.html',result)

# myprofile Api method
@csrf_exempt
@api_view(['GET'])
def myprofile_apimethod(request):
    user_id = request.GET.get('id')
    # obj = profile.objects.get(user__id=user_id)
    
    # print(obj.first_name,obj.last_name,obj.email)
    # form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    confirm = False

    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         confirm = True  
    new_obj =  profile.objects.filter(user__id=user_id)
    
    obj_serializer =ProfileSerializer(new_obj, many=True)
    # print(obj_serializer.)
    
    context = {
         'obj': obj_serializer.data,
        'confirm': confirm,
    }
    
    return Response(context)

@csrf_exempt
@api_view(['POST'])
def update_profileApi(request):
    user_id = request.POST.get('id')
    new_obj =  profile.objects.filter(user_id=user_id).first()
    confirm = False
    if request.method == 'POST':
        print(">>>>>>>>>>>>>>>>>>>>>>>>")
        print(request.data)
        serializer = ProfileUpdateSerializer(new_obj,data=request.data, partial=True)
        
        if serializer.is_valid(): 
            serializer.save()
            print(":::::::::::::::::::::::::")
        else:
            print(serializer.errors)
    return Response({'confirm':confirm})