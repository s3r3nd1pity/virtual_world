from rest_framework import serializers

from pizza.models import PizzaModel


class PizzaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    sauces = serializers.BooleanField(default=False)
    price = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return PizzaModel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance