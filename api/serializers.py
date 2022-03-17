from rest_framework import serializers

from api.models import Url


class ReturnUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('short_url',)


class CreateUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('full_url',)

    def get_or_create(self):
        defaults = self.validated_data.copy()
        identifier = defaults.pop('full_url')
        instance, created = Url.objects.get_or_create(full_url=identifier)
        if created:
            instance.generate_short_url()
            instance.save()
        return instance, created
