from django.urls import path
from . import views
from .views import DestinationListView, DestinationDetailView, DestinationCreateView, DestinationUpdateView, DestinationDeleteView

urlpatterns = [
    path('destination/', DestinationListView.as_view(), name='app1-home'),
    path('', views.about, name = 'app1-about'),
    path('destination/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('destination/new/', DestinationCreateView.as_view(), name='destination-create'),
    path('destination/<int:pk>/update/', DestinationUpdateView.as_view(), name='destination-update'),
    path('destination/<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination-delete'),
]


