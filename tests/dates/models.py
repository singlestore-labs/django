from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    pub_datetime = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField("Category", related_name="articles", through="ArticleCategory")

class Category(models.Model):
    name = models.CharField(max_length=255)


class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('article', 'category'),)
        db_table = "article_category"


class Comment(models.Model):
    article = models.ForeignKey(Article, models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date = models.DateField()
    approval_date = models.DateField(null=True)

