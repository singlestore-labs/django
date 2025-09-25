from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    published_on = models.DateField(null=True)
    categories = models.ManyToManyField("Category", related_name="articles", through="ArticleCategory")

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date = models.DateTimeField()
    approval_date = models.DateTimeField(null=True)

    def __str__(self):
        return "Comment to %s (%s)" % (self.article.title, self.pub_date)


class Category(models.Model):
    name = models.CharField(max_length=255)


class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('article', 'category'),)
        db_table = "datetimes_article_category"
        