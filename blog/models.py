from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog_slug = models.SlugField(max_length=200, unique=True, null=True)
    desc1 = models.TextField(verbose_name="Description One, Short Description", max_length=210, null=True)
    desc2 = models.TextField(verbose_name="Description Two", null=True)
    image1 = models.ImageField(upload_to="images/posts/", height_field=None, width_field=None, max_length=200, null=True, blank=True)
    brief = models.TextField(verbose_name="Subtitle or Selling Point", null=True, max_length=150, blank=True)
    desc3 = models.TextField(verbose_name="Description Three", null=True, blank=True)
    summary = models.TextField(verbose_name="Summary", null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    image2 = models.ImageField(upload_to="images/posts/", height_field=None, width_field=None, max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"


def generate_slug(sender, instance, *args, **kwargs):
    if not instance.blog_slug:
        instance.blog_slug = slugify(instance.title)

pre_save.connect(generate_slug, sender=Blog)



class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    user_name = models.CharField(verbose_name="Commentor Name", max_length=50)
    email_address = models.EmailField(verbose_name="Commentor Email Address", max_length=50)
    message = models.TextField(verbose_name="Comment Body", null=False)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = "Comments"

