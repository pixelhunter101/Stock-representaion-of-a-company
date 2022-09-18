from django.conf.urls import url 
from Backend_SQLite import views 

 
urlpatterns = [ 
    
    url(r'^api/stocks_graph$', views.stocks_graph),
    url(r'^api/add_new_stocks$', views.add_new_stocks),
    url(r'^equity/([0-9]+)$',views.equityApi),

    url(r'^daily_returns/$',views.daily_returnsApi),
    url(r'^daily_returns/([0-9]+)$',views.daily_returnsApi),
]