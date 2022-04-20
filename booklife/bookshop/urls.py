from django.urls import path
from .views import HomeView, BooksDetailView, BookCheckoutView, paymentComplete, SearchResultsListView

urlpatterns = [

    path('', HomeView.as_view(), name='users-home'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
]