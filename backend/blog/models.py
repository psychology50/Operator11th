from django.db import models
from django.utils import timezone
from django.conf import settings

class TimestampedModel(models.Model):
    create_dt = models.DateTimeField('create_dt', auto_now_add=True)
    update_dt = models.DateTimeField('update_dt', auto_now=True)

    class Meta:
        abstract = True

class Blog(TimestampedModel):
    blog_id = models.BigAutoField(primary_key=True, unique=True, verbose_name="blog_id")
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # 올려도 그만, 안 올려도 그만 // upload_to로 지정한 폴더에 img 파일을 저장해준다.
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="blog_owner") # blog를 만든 사람은 한 명이므로 OneToOneField로 지정해준다.

    def __str__(self):
        return self.title

class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True, unique=True, verbose_name="category_id")
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    def __str__(self):
        return self.name + ": " + self.description

class Post(TimestampedModel):
    '''
    모델 관리자 PostObject
    Post.objects.all() -> 기본 관리자
    Post.postobjects.all() -> 사용자 지정 관리자

    => 그니까 '게시된(published)' 게시물만 쏙쏙 골라먹겠다는 뜻. 나중에 따로 filtering 안 해줘도 됨.
    '''
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    post_id  = models.BigAutoField(primary_key=True, unique=True, verbose_name="post_id")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1, related_name='category'
    )

    title   = models.CharField(max_length=250) # 제목
    excerpt = models.TextField(null = True) # 발췌문
    content = models.TextField()
    # 슬러그는 지금 단계에선 사실 필요없지만, 슬러그는 본질적으로 URL이므로
    # 제목을 슬러그화하여 각 게시물의 고유 식별자를 사용하지 않는 방법.
    slug      = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    
    # blog와 다대일 관계
    author = models.ForeignKey( 
        Blog, on_delete=models.CASCADE, related_name='blog_posts'
    )
    # 때론 바로 게시가 되는 걸 원치 않을 수도 있으므로 options을 준다.
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )

    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager
 
    class Meta:
        ordering = ('-published', )
    
    def __str__(self):
        return self.title

class Comment(TimestampedModel):
    comment_id = models.BigAutoField(primary_key=True, unique=True, verbose_name="comment_id")
    content = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") # 어느 포스트에?
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments') # 누가 쓴 댓글?

    @property
    def short_content(self): # 댓글 미리보기 기능
        return self.comment[:10]

    def __str__(self):
        return self.comment
    
class Tag(models.Model):
    tag_id = models.BigAutoField(primary_key=True, unique=True, verbose_name="tag_id")
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, blank=True, related_name="tags")

    def __str__(self):
        return self.name