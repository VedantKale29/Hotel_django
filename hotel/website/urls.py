from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('go/', views.go, name='go'),
  #  path('', views.Hom, name='Hom'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('Hom/', views.Hom, name='Hom'),
    path('contact/', views.contact, name='contact'),
    path('explore/', views.explore, name='explore'),
    path('bb/', views.bb, name='bb'),
    path('rooms/', views.rooms, name='rooms'),
    path('homePage/', views.homePage, name='homePage'),
    

]