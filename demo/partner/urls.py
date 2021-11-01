from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('display/', views.display_product, name='display'),
    path('addpro/', views.add_product, name='addpro'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('profile/<int:pk>', views.profile, name='profile'),



    #path('register',views.register,name = "register")

]