from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField
from django.contrib.auth import get_user_model
from applications.products_framework.models import ProductType, Category, Attribute

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'email', 'username')

class CategoryBasicSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', )

class AttributesBasicSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'data_type', 'required')

class ProductTypeSerializer(ModelSerializer):
    categories = CategoryBasicSerializer(many=True, read_only=True)
    attributes = AttributesBasicSerializer(many=True, read_only=True)
    class Meta:
        model = ProductType
        fields = ('id', 'name', 'categories', 'attributes')

class ProductTypeReverseSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('id', 'name', )

class CategorySerializer(ModelSerializer):
    product_type = ProductTypeReverseSerializer(read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'product_type')


class AttributeSerializer(ModelSerializer):
    product_type = ProductTypeReverseSerializer(read_only=True)
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'data_type', 'product_type')