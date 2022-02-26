from django.urls import path, re_path
from purchase import views
from purchase.views import PurchaseList, PurchaseViewSet


## 자동으로 2개의 동작을 구현한 URL 을 만들어준다
purchase_list = views.PurchaseViewSet.as_view({
    'post': 'create',
    'get': 'list'
})


## 자동으로 4개 동작을 구현한 URL 을 만들어준다
purchase_detail = views.PurchaseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.api_root),
    path('purchase/<int:pk>/', purchase_detail, name='purchase-detail'),
    path('purchase-list/', purchase_list),
]