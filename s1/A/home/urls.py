from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('' , views.home , name='home'),
    path('add' , views.add_product , name='add'),
    path('detail/<int:product_id>' , views.product_detail , name='detail'),
    path('delete/<int:product_id>' , views.product_delete , name='delete'),
    path('update/<int:product_id>' , views.product_update , name='update'),
    path('contact/' , views.contact , name='contact')
]
