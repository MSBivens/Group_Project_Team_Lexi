from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('list', views.list, name='list'),  
    path('show_list',views.show_list, name='show_list'),  
    path('edit_list/<int:id>', views.edit_list, name='edit_list'),
    path('edit_list/home', views.show_list, name='show_list'),    
    path('update_list/<int:id>', views.update_list, name="update_list"),
    path('delete_list/<int:id>', views.destroy_list, name='delete_list'),
    # path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
    
    
    
    
    
]
