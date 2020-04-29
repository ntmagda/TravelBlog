from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=400)
    # leon_image = models.ImageField(upload_to='aboutus/authors/leon', null=True)
    leon_image = CloudinaryField('leon_image')
    magda_image = CloudinaryField('magda_image')

    # magda_image = models.ImageField(upload_to='aboutus/authors/magda', null=True)
    body = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "About Us"


class AboutUsImage(models.Model):
    property = models.ForeignKey(AboutUs, related_name='abus_images')
    # image = models.ImageField(upload_to='aboutus/authors', null=True)
    image = CloudinaryField('image')