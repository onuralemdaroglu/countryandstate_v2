from django.urls import path
from . import views 

urlpatterns = [
    path('countries/', views.CountriesListCreate.as_view(), name='country-view-create'),
    path('countries/<int:pk>/', views.CountriesRetrieveUpdateDestroy.as_view(), name='update'),
    path('countries/<str:country_code>/states/', views.CountryStateList.as_view(), name='countrystate'),
    path('states/', views.StatesListCreate.as_view(), name='states-view-create'),
    path('states/<int:pk>/', views.StatesRetrieveUpdateDestroy.as_view(), name='update')
]