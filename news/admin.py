from django.contrib import admin

from news.models import News, News_Category, ImageList_News

# Register your models here.
admin.site.register(News_Category)
admin.site.register(News)
admin.site.register(ImageList_News)