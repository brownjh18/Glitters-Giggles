from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    ServiceViewSet, BookingViewSet, GalleryViewSet,
    BlogViewSet, NewsletterViewSet, ContactViewSet, UserViewSet
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'newsletter', NewsletterViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]