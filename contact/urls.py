from django.urls import path
from .views import ContactListCreateView, ContactDetailsView

app_name = "contact"

urlpatterns = [
    path("contact/", ContactListCreateView.as_view(), name="contact"),
    path("<int:id>/", ContactDetailsView.as_view(), name="contact-detail"),
]
