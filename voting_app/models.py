from django.db import models

# Create your models here.
from django.urls import reverse

class Vote(models.Model):
    title        = models.CharField(max_length = 50, blank=False)
    start_date   = models.DateTimeField(blank=False)
    end_date     = models.DateTimeField(blank=False)
    votes_to_win = models.IntegerField(blank=False)
    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/vote/{self.id}"

class Character(models.Model):
    name  = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img')
    age   = models.IntegerField()
    vote  = models.ManyToManyField(Vote, through='VoteForCharacter')
    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
    def __str__(self):
        return self.name
        #return str(self.url)

class VoteForCharacter(models.Model):
    vote         = models.ForeignKey(Vote, on_delete=models.CASCADE)
    character    = models.ForeignKey(Character, on_delete=models.CASCADE)
    #character    = models.OneToOneField(Character, on_delete=models.CASCADE)
    votes_number = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Голосование за персонажа'
        verbose_name_plural = 'Голосования за персонажей'
        unique_together = ('vote', 'character',)

    def __str__(self):
        return 'Голосование {0} за {1}'.format(self.vote.title, self.character.name)

