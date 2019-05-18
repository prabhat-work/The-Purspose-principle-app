from django.urls import path,include
from . import views
 
urlpatterns =[ 
    path('create',views.create, name='create'),  #making new futn create forwareded to views of products
    path('<int:product_id>', views.detail , name='detail'),
    # path('<int:product_id>', views.home , name='home'),
    # path('<int:product_id>/upvote', views.upvote , name='upvote'),
]
