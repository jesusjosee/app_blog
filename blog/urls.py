from django.urls import path
from . import views

# name of app , it used with namespace (I used to without namespace in the urlpatterns main)
app_name='blog'

# urls patterns
urlpatterns=[
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name = 'post_list' ),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
]