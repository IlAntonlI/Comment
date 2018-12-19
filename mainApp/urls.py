from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('', views.post_single, name="content"),
    path('comment-vote/<int:comment_id>', views.vote_view, name='vote'),
]
