# models.py

from django.db import models

#Makeup-artist
class MakeupService(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    image1 = models.ImageField(upload_to='makeup_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='makeup_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='makeup_images/', null=True, blank=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=50, default='')
    rating = models.DecimalField(max_digits=4, decimal_places=2 , default=0)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    def update_rating(self, new_rating):
        total_ratings = self.ratings.count()
        current_total = self.rating * total_ratings
        new_total = current_total + new_rating
        new_average = new_total / (total_ratings + 1)
        self.rating = round(new_average, 2)
        self.save()


    def __str__(self):
        return self.name

class Image(models.Model):
    makeup_service = models.ForeignKey(MakeupService, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='makeup_images/')

    def __str__(self):
        return f"Image for {self.makeup_service.name}"
class Rating(models.Model):
    makeup_service = models.ForeignKey(MakeupService, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

#Djs


class DjsServices(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    image1 = models.ImageField(upload_to='makeup_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='makeup_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='makeup_images/', null=True, blank=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=50, default='')
    rating = models.DecimalField(max_digits=4, decimal_places=2 , default=0)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    def update_rating(self, new_rating):
        total_ratings = self.ratings.count()
        current_total = self.rating * total_ratings
        new_total = current_total + new_rating
        new_average = new_total / (total_ratings + 1)
        self.rating = round(new_average, 2)
        self.save()


    def __str__(self):
        return self.name

class ImageDjs(models.Model):
    Djs_services = models.ForeignKey(DjsServices, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Djs_images/')

    def __str__(self):
        return f"Image for {self.Djs_services.name}"
class RatingDjs(models.Model):
    Djs_services = models.ForeignKey(DjsServices, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)


#Traiteur

class CatererService(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    image1 = models.ImageField(upload_to='caterer_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='caterer_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='caterer_images/', null=True, blank=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=50, default='')
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    price_per_Table = models.DecimalField(max_digits=8, decimal_places=2)

    def update_rating(self, new_rating):
        total_ratings = self.ratings.count()
        current_total = self.rating * total_ratings
        new_total = current_total + new_rating
        new_average = new_total / (total_ratings + 1)
        self.rating = round(new_average, 2)
        self.save()

    def __str__(self):
        return self.name

class ImageCar(models.Model):
    caterer_service = models.ForeignKey(CatererService, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='caterer_images/')

    def __str__(self):
        return f"Image for {self.caterer_service.name}"

class RatingCar(models.Model):
    caterer_service = models.ForeignKey(CatererService, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)


