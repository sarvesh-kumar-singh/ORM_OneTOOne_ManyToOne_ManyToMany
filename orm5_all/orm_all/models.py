from django.db import models

from django.contrib.auth.models import User


class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    page_name=models.CharField(max_length=50)
    page_cat=models.CharField(max_length=50)
    page_post_date=models.DateField()


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_name=models.CharField(max_length=50)
    post_cat=models.CharField( max_length=50)
    post_publish_date=models.DateField()

class Song(models.Model):
    user=models.ManyToManyField(User)
    song_title=models.CharField(max_length=250)
    song_cat=models.CharField(max_length=100)
    song_publish_date=models.DateField()
    # song_duration=models.IntegerField()

    def written_by(self):
        return " ".join([str(p) for p in self.user.all()])

                                    