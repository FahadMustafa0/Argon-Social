from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from profiles.models import profile
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core.files import storage
from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from .forms import PostForm
from itertools import chain

@csrf_exempt
def post_create_view(request):
    if request.POST:
        form = PostForm(data=request.POST, files=request.FILES)
        # form.instance.author = get_author(self.request.user)
        if form.is_valid():
            obj = form.save()
            # obj.author = request.user
            obj.author1= profile.objects.get(user=request.user)
            obj.save()
            return redirect(post_of_following_profiles)
        else:
            print(form.errors)

        context ={
            'form': form
        }
    else:
        form = PostForm()

        context ={
            'form': form
        }

    return render(request,'posts/postcreate.html',context)


# getting all posts

class PostListView(View):
    def get(self,request,*args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        
        context = {
            'post_list': posts,
            
                  }
        return render(request, 'posts/postlist.html',context)


def post_of_following_profiles(request):

    # get logged in user profile
    my_profile=profile.objects.get(user=request.user)
   
    # check who we are post_of_following
    # users=[user for user in my_profile.following.all()]
    users=my_profile.following.all()
    

    usaaar=[]
    # the users who we are not following
    for user1 in User.objects.all():
        if user1 not in my_profile.following.all() and not user1==request.user:
                usaaar.append(user1)
    
    # not_follow = [user for user in my_profile.following.all()]

    # initial values for variables
    allposts=[]
    public_posts=[]

    
    

    # get the posts of the people who we are following
    for u in users:
        # print(u)
        p=profile.objects.get(user=u)
        p_posts=p.post_set.all()
        allposts.append(p_posts)
    

         # get the public posts of the people who we are not following
    for u1 in usaaar:
        p1=profile.objects.get(user=u1)
        p_posts1=p1.post_set.all()
        for pp in p_posts1:
            if not pp.private:
                public_posts.append(pp)
    allposts.append(public_posts)   
    print(allposts)
        

    # getting all the users excluding me
     
    # us=[u1 for u1 in User.objects.all().exclude(id=request.user.id)]
    
    # getting posts of the other people public/private
    qs=None
    # My posts
    my_posts=my_profile.profile_posts()
    allposts.append(my_posts)
    
    # sort the posts in order and unpaking the queryset because posts are showing as queryset
    if len(allposts)>0:
        qs=sorted(chain(*allposts),reverse=True, key= lambda obj1 : obj1.created_on)
   
    return render(request,'main1.html',{'unpacked': qs })