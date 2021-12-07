from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core.files import storage
from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from .forms import PostForm

@csrf_exempt
def post_create_view(request):
    if request.POST:
        form = PostForm(data=request.POST, files=request.FILES)
        # form.instance.author = get_author(self.request.user)
        if form.is_valid():
            obj = form.save()
            obj.author = request.user
            obj.save()
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



class PostListView(View):
    def get(self,request,*args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        
        context = {
            'post_list': posts,
            
                  }
        return render(request, 'posts/postlist.html',context)

