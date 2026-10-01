
from django.urls import path
from . views import *

urlpatterns = [

    path('newproduct/', newproduct, name='newproduct'),

    path('saveorder/', saveorder, name='saveorder'),

    path('productlist/',productlist, name='productlist'),

    path('updateproductform/',updateproductform,name='updateproductform'),

    path('updateProduct/',updateProduct,name='updateProduct'),

    path('deleteProduct/',deleteProduct,name='deleteProduct'),

]
