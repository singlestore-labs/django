from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    friends = models.ManyToManyField("self", through="PersonFriend")

class PersonFriend(models.Model):
    from_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="from_person"
    )
    to_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="to_person"
    )

    class Meta:
        unique_together = (('from_person', 'to_person'),)
        db_table = "test_runner_person_friend"


# A set of models that use a non-abstract inherited 'through' model.
class ThroughBase(models.Model):
    person = models.ForeignKey(Person, models.CASCADE)
    b = models.ForeignKey("B", models.CASCADE)


class Through(ThroughBase):
    extra = models.CharField(max_length=20)


class B(models.Model):
    people = models.ManyToManyField(Person, through=Through)
