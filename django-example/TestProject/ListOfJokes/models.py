from django.db import models


class User(models.Model):
    objects = models.Manager()

    username = models.CharField(max_length=64)
    password = models.CharField(max_length=36)
    rating = models.FloatField

    def __str__(self):
        return self.username


class StartPhrases(models.Model):
    objects = models.Manager()

    text = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    phrase_rating = models.FloatField

    def __str__(self):
        return self.text


class Comments(models.Model):
    objects = models.Manager()

    comment_text = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    related_phrase = models.ForeignKey(StartPhrases, on_delete=models.PROTECT)
    comment_rating = models.FloatField

    def __str__(self):
        return self.comment_text



