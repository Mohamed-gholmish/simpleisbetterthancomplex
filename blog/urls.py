from django.urls import path
app_name='blog'

from .import views
urlpatterns=[
path('',views.all_posts),

path('<int:post_id>',views.post_detail)

   ]
