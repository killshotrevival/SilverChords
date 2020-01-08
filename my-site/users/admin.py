from django.contrib import admin
from .models import profile, quote, verification, helpinfo

admin.site.register(profile)
admin.site.register(quote)
admin.site.register(verification)
admin.site.register(helpinfo)

