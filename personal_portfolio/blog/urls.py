from django.urls import path

from .views import PostDetail ,blog


urlpatterns = [
    path('', blog, name='blog'),
    path('/<int:post_id>/', PostDetail.as_view(), name='post'),
]