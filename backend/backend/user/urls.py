from django.urls import path

# from . import views
#
# urlpatterns = [
#     path('login/', views.login, name="login"),
#     path('logout/', views.logout, name="logout"),
#     path('signup/', views.signup, name='signup'),
# ]

from .views import SignUpUserView

urlpatterns = [
    path('signup/', SignUpUserView.as_view(), name='register'),
]
