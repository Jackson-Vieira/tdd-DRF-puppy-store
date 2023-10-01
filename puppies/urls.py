from django.urls import path
from puppies import views

urlpatterns = [
    path('api/v1/puppies', views.get_post_puppies,
         name="get_post_puppies"),
    path('api/v1/puppies/<int:pk>', views.get_delete_update_puppy,
         name="get_delete_update_puppy")
]
