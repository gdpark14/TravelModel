from django.urls import path
from .views import signup,append_revise,profile_view
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('append_revise',append_revise,name='append_revise'),
    path('profile_view/<str:person_name>',profile_view,name='profile_view'),

]