"""
Multiple many-to-many relationships between the same two tables

In this example, an ``Article`` can have many "primary" ``Category`` objects
and many "secondary" ``Category`` objects.

Set ``related_name`` to designate what the reverse relationship is called.
"""

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    primary_categories = models.ManyToManyField(
        Category, related_name="primary_article_set", through="ArticleCategory"
    )
    secondary_categories = models.ManyToManyField(
        Category, related_name="secondary_article_set", through="ArticleCategoryS"
    )

    class Meta:
        ordering = ("pub_date",)

    def __str__(self):
        return self.headline

class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('article', 'category'),)
        db_table = "m2m_multiple_article_category"


class ArticleCategoryS(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('article', 'category'),)
        db_table = "m2m_multiple_article_category_second"
