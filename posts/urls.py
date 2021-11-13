from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PostsPageView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("posts/", login_required(PostsPageView.as_view()), name="posts"),
]
