from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, ListAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from applications.products_framework.models import ProductType, Category, Attribute
from .serializers import UserSerializer, ProductTypeSerializer, CategorySerializer, AttributeSerializer

User = get_user_model()

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, *kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user_detail'

class ProductTypeList(ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    name = 'product-type-list'

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class AttributeList(ListAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    name = 'attribute-list'