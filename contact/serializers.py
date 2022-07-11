from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            "id",
            "first_name",
            "last_name",
            "country_code",
            "phone_number",
            "contact_image",
            "is_favorite",
        )
