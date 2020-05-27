

from django.urls import reverse

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


STATUS_CHOICES = (
    ("RA", "RECENTLY ADDED"),
    ("MR", "MOST READ"),
    ("TR", "TOP RATED"),
)

# REVIEW_POINT_CHOICES = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))


class Book(models.Model):
    
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="book")
    publish_data = models.DateField()
    purchase_site = models.URLField(max_length=1000, default=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    # 조회수
    views_count = models.IntegerField(default=0)

    class Meta:
        ordering = [
            "title",
        ]

    def __str__(self):
        return self.title

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.point_average()
            # print(review.rating_average())
            return all_ratings / len(all_reviews)
        return 0

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})
        # return "/books/{}/".format(self.pk)

    @property
    def update_counter(self):
        self.views_count = self.views_count + 1
        self.save()


class Review(models.Model):
    point = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        "books.Book", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"{self.content} - {self.book}"  #  return self.review, return self.room 등등
        )

    def point_average(self):
        point_count = (
            Review.objects.filter().count()
        )  # book, book_id, content, id, point, user, user_id
        avg = self.point / point_count
        return round(avg, 2)

    def get_absolute_url(self):
        return self.book.get_absolute_url() + "#review-id-{}".format(self.pk)



