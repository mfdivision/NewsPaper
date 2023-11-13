from django.db import models

from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    author_rate = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).aggregate(pr=Sum('post_rate'))['pr']
        comments_rating = Comments.objects.filter(user=self.user).aggregate(cr=Sum('comment_rate'))['cr']
        posts_comments_rating = Comments.objects.filter(post__author=self).aggregate(pcr=Sum('comment_rate'))['pcr']

        self.author_rate = post_rating * 3 + comments_rating + posts_comments_rating
        self.save()
        print(self.author_rate)


class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    NEWS = 'N'
    POSTS = 'P'
    POST_TYPE_CHOICES = [
        (NEWS, 'Новость'),
        (POSTS, 'Статья')
    ]

    name = models.CharField(max_length=50, blank=False)
    text = models.CharField(max_length=1000000)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, )
    post_rate = models.IntegerField(default=0)
    post_type = models.CharField(max_length=1, choices=POST_TYPE_CHOICES, default='Новость')
    post_categories = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        preview = self.text[:124] + '...'
        return preview

    def post_like(self):
        self.post_rate += 1
        self.save()

    def post_dislike(self):
        self.post_rate -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_rate = models.IntegerField(default=0)

    def comment_like(self):
        self.comment_rate = self.comment_rate + 1
        self.save()

    def comment_dislike(self):
        self.comment_rate = self.comment_rate - 1
        self.save()
