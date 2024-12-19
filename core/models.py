from django.db import models
from django.contrib.auth.models import User

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    city = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.city}"

# SocialProfile model
class SocialProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=[('user', 'User'), ('brand', 'Brand'), ('creator', 'Creator')])
    profiles = models.ManyToManyField(Profile, related_name="social_profiles")

    def __str__(self):
        return f"{self.username} ({self.type})"

# Membership model
class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('free', 'Free Membership'),
        ('trial', 'Trial Membership'),
        ('paid', 'Paid Membership'),
    ]

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="membership")
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES, default='free')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.profile.user.username} - {self.membership_type} Membership"

# SubscriptionPlan model
class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=20, choices=PLAN_CHOICES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Subscription model
class Subscription(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name="subscriptions")
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, related_name="subscriptions")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    auto_renew = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.membership.profile.user.username} - {self.plan.name}"

# Post model for SocialProfile
class Post(models.Model):
    social_profile = models.ForeignKey(SocialProfile, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"Post by {self.social_profile.username} - {self.likes} Likes"