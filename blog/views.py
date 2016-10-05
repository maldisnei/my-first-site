from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm
def index(request):
    postes = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request,'blog/index.html',{'postes':postes})


def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/detail.html',{'post':post})
    
def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.auth = request.user
            post.published_date = timezone.now()
            post=form.save()
            return redirect('blog.views.detail', pk=post.pk )
    else:
        form = PostForm()

    return render(request,'blog/post_draft.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth=request.user
            post.published_date=timezone.now()
            post=form.save()
            return redirect('blog.views.detail', pk=post.pk)
    else:
        form=PostForm(instance=post)

    return render(request,'blog/post_draft.html',{'form':form})
