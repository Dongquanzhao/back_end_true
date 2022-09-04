from django.views.static import serve
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AliPayView

import xadmin
from .settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewSet

# Create a router and register our viewsets with it.

router = DefaultRouter()

# 配置goods的路由
router.register(r'goods', GoodsListViewSet, basename='goods')

# 配置categories的路由
router.register(r'categorys', CategoryViewSet, basename='categories')

# 配置轮播图路由
router.register(r'banners', BannerViewSet, basename='banners')

# 配置首页商品系列路由
router.register(r'indexgoods', IndexCategoryViewSet, basename='indexgoods')

# 配置短信验证码路由
router.register(r'codes', SmsCodeViewSet, basename='codes')

# 配置注册路由
router.register(r'users', UserViewSet, basename='users')

# 配置收藏路由
router.register(r'userfavs', UserFavViewSet, basename='userfavs')

# 配置留言路由
router.register(r'messages', LeavingMessageViewSet, basename='messages')

# 配置收货地址路由
router.register(r'address', AddressViewSet, basename='address')

# 配置购物车路由
router.register(r'shopcarts', ShoppingCartViewSet, basename='shopcarts')

# 配置下订单路由
router.register(r'orders', OrderViewSet, basename='orders')

# 支付宝结果返回接口
url(r'^alipay/return/', AliPayView.as_view(), name='alipay')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 商品列表页
    url(r'^', include(router.urls)),

    # 文档路由
    url(r'docs/', include_docs_urls(title='水果商店')),

    # JWT认证路由
    url(r'^login/', obtain_jwt_token),

    # 第三方登录
    url('', include('social_django.urls', namespace='social'))

]
