from django.contrib import admin
from myblogapp.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('body', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['body']
    fieldsets = [
        (None,               {'fields': ['body']}),
        ('Date information', {'fields': ['body'], 'classes': ['collapse']}),
    ]


admin.site.register(Post, PostAdmin)