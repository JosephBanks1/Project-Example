from django.db import models
from django.contrib.auth.models import User

class Joke(models.Model):
    setup = models.CharField(max_length=255)
    delivery = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jokes", default=None, null=True)

    def __str__(self):
        return f"Joke: {self.setup} Punchline: {self.delivery}"

class Dog(models.Model):
    url = models.TextField(default="")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dogs", default=None, null=True)    

    def __str__(self):
        return f"Picture URL: {self.url}"