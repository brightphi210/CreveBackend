
from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.endpoint, name="enpoint"),
    path('api/creative/register/', views.CreativeRegistrationView.as_view(),
         name="creativeRegistration"),


    path('api/creative/<str:pk>/',
         views.CreativeUpdate.as_view(), name="creativeUpdate"),


    path('api/creativeProfile/', views.GetCreativeProfileView.as_view(),
         name="creativeProfile"),


    path('api/creativeProfile/<str:pk>/',
         views.CreativeEdithProfile.as_view(), name="CreativeEdithProfile"),


    path('api/user/register/', views.UserRegistrationView.as_view(),
         name="creativeRegistration"),


    path('api/products/', views.ProductGet.as_view(), name="productCreative"),
    path('api/products/create/', views.ProductGetCreate.as_view(),
         name="productCreative"),


    path('api/products/<str:pk>/',
         views.ProductGetUpdateDelete.as_view(), name="productUpdateDelete"),

    path('api/creativeProducts/',
         views.ProductUser.as_view(), name='user-products'),

]
