

from django.urls import include, path
from . import views
urlpatterns = [
    path('all-info/',views.Info_API.as_view()),
    path('all-info/<slug:info_slug>',views.Each_Info.as_view()),
]
