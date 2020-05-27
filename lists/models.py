from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class ListManager(models.Manager):
    def new_or_get(self, request):
        list_id = request.session.get("list_id", None)
        qs = self.get_queryset().filter(id=list_id)
        if qs.count() == 1:
            new_obj = False
            list_obj = qs.first()
            if request.user.is_authenticated and list_obj.user is None:
                list_obj.user = request.user
                list_obj.save()
        else:
            list_obj = List.objects.new(user=request.user)
            new_obj = True
            request.session["list_id"] = list_obj.id
        return list_obj, new_obj

    def new(self, user=None):
        # print(user)
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class List(models.Model):

    """ List Model Definition """

    user = models.ForeignKey(User, related_name="lists", on_delete=models.CASCADE)
    books = models.ManyToManyField("books.Book", related_name="lists", blank=True)

    objects = ListManager()

    def __str__(self):
        return str(self.id)
