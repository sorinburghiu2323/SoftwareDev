from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

# Post Class
from django.utils import timezone


# User Class
class CustomUserManager(BaseUserManager):
	"""
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

	def create_user(self, email, password, **extra_fields):
		"""
        Cate and save a User with the given email and password.
        """
		if not email:
			raise ValueError(_("The Email must be set"))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		"""
        Create and save a SuperUser with the given email and password.
        """
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		extra_fields.setdefault("is_active", True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError(_("Superuser must have is_staff=True."))
		if extra_fields.get("is_superuser") is not True:
			raise ValueError(_("Superuser must have is_superuser=True."))
		return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	password = models.CharField(blank=True, max_length=255)
	username = models.CharField(max_length=255, unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	points = models.IntegerField(default=0)
	is_teacher = models.BooleanField(default=False)
	hide_leaderboard = models.BooleanField(default=False)

	# more fields
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(default=timezone.now)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email


# Community Class
class Community(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)  # Creator of the community
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id

	def serialize(self):
		return {
			"user"       : self.user,
			"name"       : self.name,
			"description": self.description,
			"created_at" : self.created_at,
		}


class Post(models.Model):
	class PostType(models.TextChoices):
		DISCUSSION = "discussion"
		QUESTION = "question"

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	community = models.ForeignKey(Community, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, unique=True)
	description = models.TextField(default=0)
	post_type = models.CharField(max_length=20, choices=PostType.choices, default=PostType.DISCUSSION)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id

	def serialize(self):
		return {
			"user"       : self.user,
			"community"  : self.community,
			"title"      : self.title,
			"description": self.description,
			"post_type"  : self.post_type,
			"created_at" : self.created_at,
		}


# PostLike Class
class PostLike(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id

	def serialize(self):
		return {
			"user"      : self.user,
			"post"      : self.post,
			"created_at": self.created_at,
		}


# PostComment Class
class PostComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.TextField(max_length=255, unique=False)
	is_approved = models.BooleanField(default=0)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id

	def serialize(self):
		return {
			"user"       : self.user,
			"post"       : self.post,
			"comment"    : self.comment,
			"is_approved": self.is_approved,
			"created_at" : self.created_at,
		}


# PostCommentLike Class
class PostCommentLike(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post_comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id

	def serialize(self):
		return {
			"user"        : self.user,
			"post_comment": self.post_comment,
			"created_at"  : self.created_at,
		}
