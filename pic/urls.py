from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from . import views
urlpatterns = [
    # path('upload_handle', views.upload_handle),
    path('show_imgs', views.show_imgs),
    path('image_field', views.image_field),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]