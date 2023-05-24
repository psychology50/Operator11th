from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect,  HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer


# Create your views here.

def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-create_dt')

    print(Post.objects.filter(post_id=1))
    Post.objects.get(post_id=1)

    print(Post.objects.filter().order_by('-create_dt'))
    print(Post.objects.filter().order_by('-create_dt').query)

    paginator = Paginator(posts, 5) # 객체, 끊어내는 개수
    pageNum = request.GET.get('page') # 끊은 객체들을 dict타입으로 저장했다가 pageNumber로써 값을 조회할 수 있게 함
    posts = paginator.get_page(pageNum)

    return render(request, 'index.html', {'posts':posts})

class CreatePostView(APIView):
    # Flow.
    # 1. Post 모델을 저장하기 위해 Client 측에서 POST 요청을 보낸다.
    # 2. Client 측에서 보낸 데이터는 JSON 형식으로 보낸다.
    # 3. request에는 Post를 저장하기 위한 데이터가 모두 담겨있다고 가정
    def post(self, request):
        print(f"===== 1. request : {request} =====")

        serializer = PostSerializer(data=request.data)  # client 측에서 보낸 data를 역직렬화
        print(f"===== 2. serializer : {serializer} =====")

        serializer.is_valid(raise_exception=True)  # 역직렬화 한 데이터가 유효한지 검사 (유효하지 않으면 에러)
        print(f"===== 3. serializer.is_valid : {serializer.is_valid} =====")

        serializer.save() # 역직렬화 한 데이터를 DB에 저장

        print(f"===== 4. serializer.data : {serializer.data} =====")
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # 저장한 데이터를 다시 직렬화 하여 client 측에 응답

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.blog
            post.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
    else:
        form = PostForm()
        return HttpResponseRedirect(reverse('post_create'))

def post_list(request):
    posts = Post.postobjects.all()
    print(f" post_list : {posts} ")
    return HttpResponse('Post list.')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(f" post_detail : {post} ")
    return HttpResponse('Post detail.')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.blog
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return HttpResponse('Post update.')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('home')