
from django.urls import path
from django import views
from foodapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('prod_cat<slug:c_slug>/',views.home,name="prod_cat"),
    path('details<slug:c_slug>/<slug:product_slug>',views.productdetails,name="details"),
     path('/<str:name>/',views.itemdetails,name="items"),
     path('category',views.category,name='category'),
     path('c_id',views.c_id,name='c_id'),
      path('searchitems',views.searchitems,name="searchitems"),
    path('addcart/<int:product_id>',views.addcart,name='addcart'),
    path('min/<int:product_id>',views.min,name='min'),
    path('deleteelement/<int:product_id>',views.deleteelement,name='deleteelement'),
     path('cartdetails',views.cartdetails,name='cartdetails'),
     path('testcart',views.testcart,name='testcart'),
      path('reg',views.reg,name='reg'),
      path('login',views.login,name='login'),
      path('logout',views.logout,name='logout'),
    
    path('touchdisplay/<int:pk_id/',views.touchdisplay,name='touchdisplay'),
   ## path('home/<int:id/',views.home,name='home'),
  
    
     
    

    

    
   
   
]