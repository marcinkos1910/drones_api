from django.db import models


class Drone(models.Model):
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey('DroneCategory', on_delete=models.CASCADE, related_name='drones')
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class DroneCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Drone_categories'

    def __str__(self):
        return self.name


GENDER_CHOICES = (('M', 'male'), ('F', 'female'))


class Pilot(models.Model):
    name = models.CharField(max_length=150, default='', blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='M')
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Competition(models.Model):
    pilot = models.ForeignKey('Pilot', on_delete=models.CASCADE)
    drone = models.ForeignKey('Drone', on_delete=models.CASCADE)
    distance = models.IntegerField()
    achievement_date = models.DateTimeField()

    class Meta:
        ordering = ('-distance',)

    def __str__(self):
        return f'{self.distance}'
