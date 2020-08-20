from django.urls import path, include
from .views import index,create,detail,delete,update,my_index,create_comment,delete_comment,search_index,like,location

urlpatterns = [
    path('',index,name='index'),
    path('my_index/',my_index,name='my_index'),
    path('search_index/',search_index,name='search_index'),
    
    path('create/',create,name="create"),
    path('location/<str:location_name>/',location,name="location"),
    path('detail/<int:jss_id>',detail,name="detail"),
    path('delete/<int:jss_id>',delete,name="delete"),
    path('update/<int:jss_id>',update,name="update"),
    
    path('create_comment/<int:jss_id>/',create_comment,name="create_comment"),
    path('delete_comment/<int:jss_id>/<int:comment_id>/',delete_comment,name="delete_comment"),
    path('like/<int:jss_id>/',like,name="like"),
]