from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import MenuModel, CategoryModel, MenuItemModel


class MenuSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return MenuModel.objects.create(**validated_data)

    class Meta:
        model = MenuModel
        fields = "__all__"


class CategorySerializer(serializers.Serializer):
    id = ReadOnlyField()
    name = serializers.CharField(max_length=50)
    menu_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return CategoryModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class MenuItemSerializer(serializers.Serializer):
    id = ReadOnlyField()
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255, allow_blank=True)
    category_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return MenuItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.name)
        instance.save()
        return instance
