from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm
from .models import Comments 

# Create your views here.
def  getPosts(request):
    template_name='postapp/list.html'
    posts = Post.objects.all()
    context={"postlar":posts }
    return render(request, template_name=template_name , context=context)


def getPost(request, pk):
    
    template_name = 'postapp/detail.html'
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    tags = post.tags.all()
    print(tags)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = request.POST.get("parentId")
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comments.objects.get(pk=parent_id)
            if parent_obj:
                cf = comment_form.save(commit=False)
                cf.parent = parent_obj
                cf.post = post
                cf.save()
                comment_form = CommentForm()
    context={"post":post, "comment_form":comment_form, "comments":comments, "tags":tags}
    return render(request=request, template_name=template_name , context=context)

def getPostsByTag(request, tagName):
    filter = True
    template_name='postapp/list.html'
    posts = Post.objects.filter(tags__name=tagName).all()
    context={"posts":posts, "filter":filter}
    return render(request, template_name=template_name , context=context)

def addPost(request):
    pass

def about(request):
    template_name = 'about.html'
    return render(request, template_name=template_name , )
