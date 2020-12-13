from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return f"id={self.id}. category_name={self.category_name}"

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    post_title = models.CharField(max_length=255)
    post_price = models.CharField(max_length=255)
    post_description = models.TextField()
    post_email = models.CharField(max_length=255)
    # post_photo = models.CharField(max_length=255)
    # post_date = models.CharField(max_length=255)
    # post_location = models.CharField(max_length=255)

    def __str__(self):
        return f"id={self.id}. post_title={self.post_title}, post_price={self.post_price}"