from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    sites = models.ManyToManyField("Site", through="ArticleSite")
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField("model_package.Publication", blank=True, through="Articlemodel_package")


class ArticleSite(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('article', 'site'),)
        db_table = "model_package_article_site"


class Articlemodel_package(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    publication = models.ForeignKey("model_package.Publication", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('article', 'publication'),)
        db_table = "model_package_article_publications"
