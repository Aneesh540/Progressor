from django.db import models
from django.utils import timezone

class Directory(models.Model):
    name = models.CharField(max_length=50, blank=False)
    necessary = models.BooleanField(default=False)

    def __str__(self):
        return "{0} | {1}".format(self.name,self.id)



class Todoentry(models.Model):
    # null=True for allowing null in database, blank=True to allow blank in form
    basedir = models.ForeignKey(Directory,on_delete=models.CASCADE)

    entry = models.CharField(max_length=100,blank=False,null=False)

    create_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(blank=True, null=True)

    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "{0} | {1}".format(self.entry, self.basedir.name)


class Details(models.Model):

    which_entry = models.ForeignKey(Todoentry,on_delete=models.CASCADE)
    subtask = models.CharField(max_length=100,blank=False,null=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.subtask
