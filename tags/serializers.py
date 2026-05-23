from rest_framework import serializers
from django.utils.text import slugify
from unidecode import unidecode
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

    def create(self, validated_data):
        name = validated_data.get('name')
        latin_name = unidecode(name)
        validated_data['slug'] = slugify(latin_name)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            latin_name = unidecode(validated_data['name'])
            validated_data['slug'] = slugify(latin_name)
        return super().update(instance, validated_data)