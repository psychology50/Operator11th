from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-create_dt')

    paginator = Paginator(posts, 5) # 객체, 끊어내는 개수
    pageNum = request.GET.get('page') # 끊은 객체들을 dict타입으로 저장했다가 pageNumber로써 값을 조회할 수 있게 함
    posts = paginator.get_page(pageNum)

    return render(request, 'index.html', {'posts':posts})