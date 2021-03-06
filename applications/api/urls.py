from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_views

from .views import CustomObtainAuthToken, UserDetail, ProductTypeList, CategoryList, AttributeList

urlpatterns = [
    url(r'^get_auth_token/$', CustomObtainAuthToken.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name=UserDetail.name),
    url(r'^product-type/$', ProductTypeList.as_view(), name=ProductTypeList.name),
    url(r'^category/$', CategoryList.as_view(), name=CategoryList.name),
    url(r'^attribute/$', AttributeList.as_view(), name=AttributeList.name),
]

