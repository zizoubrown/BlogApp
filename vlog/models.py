from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)
	profile_info = models.TextField(max_length=150, null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	favorites = models.ManyToManyField(Post)
	picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Picture')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		SIZE = 250, 250

		if self.picture:
			pic = Image.open(self.picture.path)
			pic.thumbnail(SIZE, Image.LANCZOS)
			pic.save(self.picture.path)

	def __str__(self):
		return self.user.username
		
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()