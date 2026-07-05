from django.contrib import admin
from first_app.models import AccessRecord, Topic, WebPage, UserProfileInfo

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(UserProfileInfo)