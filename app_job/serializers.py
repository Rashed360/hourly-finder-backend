from rest_framework.serializers import ModelSerializer
from .models import Ingredient, Customer, Order


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ['id']


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('deliveryAddress','phone','paymentType')


class OrderSerializer(ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        customer_data = validated_data.pop('customer')

        ingredients = IngredientSerializer.create(IngredientSerializer(), validated_data=ingredients_data)
        customer = CustomerSerializer.create(CustomerSerializer(), validated_data=customer_data)

        order, created = Order.objects.update_or_create(
            ingredients=ingredients,
            customer=customer,
            user=validated_data.pop('user'),
            price=validated_data.pop('price'),
            orderTime=validated_data.pop('orderTime'),
        )
        return order
