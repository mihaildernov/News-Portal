from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        self.author_rating = 0
        for post in Post.rating.validators:
            self.author_rating += post * 3
        for comment in Comment.rating.validators:
            self.author_rating += comment

    def __str__(self):
        return f'{self.user.username}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, through='SubscribersCategory')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0)
    time_in = models.DateTimeField(auto_now_add=True)
    GROUP_CHOICES = (('A', 'Article'), ('N', 'News'))
    group = models.CharField(max_length=1, choices=GROUP_CHOICES)

    def like(self, amount=1):
        self.rating += amount
        self.save()

    def dislike(self):
        self.like(-1)

    def preview(self):
        first_text = self.text
        return first_text[:124], '...'

    def __str__(self):
        return f'{self.title.title()}: {self.text[:10]}'

    def get_absolute_url(self):
        return f'/newss/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title_post}: {self.category.name}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self, amount=1):
        self.rating += amount
        self.save()

    def dislike(self):
        self.like(-1)


class SubscribersCategory(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}: {self.subscriber}'