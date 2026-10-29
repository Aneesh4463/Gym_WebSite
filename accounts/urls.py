from django.urls import path
from .views import OwnerLoginView, OwnerLogoutView,OwnerDashboardView

urlpatterns = [
    path('owner-login/', OwnerLoginView.as_view(), name='owner_login'),
    path('owner-logout/', OwnerLogoutView.as_view(), name='owner_logout'),
    path('owner-dashboard/', OwnerDashboardView.as_view(), name='owner_dashboard'),
]
