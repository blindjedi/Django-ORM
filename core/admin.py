from django.contrib import admin
from .models import Profile, SocialProfile, Membership, SubscriptionPlan, Subscription, Post

# Register your models here
admin.site.register(Profile)
admin.site.register(SocialProfile)
admin.site.register(Membership)
admin.site.register(SubscriptionPlan)
admin.site.register(Subscription)
admin.site.register(Post)