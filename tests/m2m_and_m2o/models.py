"""
Many-to-many and many-to-one relationships to the same table

Make sure to set ``related_name`` if you use relationships to the same table.
"""
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)


class Issue(models.Model):
    num = models.IntegerField()
    cc = models.ManyToManyField("User", blank=True, related_name="test_issue_cc", through="IssueUser")
    client = models.ForeignKey(User, models.CASCADE, related_name="test_issue_client")

    class Meta:
        ordering = ("num",)

    def __str__(self):
        return str(self.num)


class IssueUser(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('issue', 'user'),)
        db_table = "m2m_and_m2o_issue_user"


class StringReferenceModel(models.Model):
    others = models.ManyToManyField("StringReferenceModel", through="StringReferenceModelStringReferenceModel")


class StringReferenceModelStringReferenceModel(models.Model):
    from_stringreferencemodel = models.ForeignKey(StringReferenceModel, on_delete=models.CASCADE, related_name="from_stringreferencemodel")
    to_stringreferencemodel = models.ForeignKey(StringReferenceModel, on_delete=models.CASCADE, related_name="to_stringreferencemodel")

    class Meta:
        unique_together = (('from_stringreferencemodel', 'to_stringreferencemodel'),)
        db_table = "m2m_and_m2o_stringreferencemodel_stringreferencemodel"
