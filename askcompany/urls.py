from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='root.html'), name='root.html')
    re_path('', TemplateView.as_view(template_name='root.html'), name='root.html') # re_path : url 을 자동으로 여기로 리턴
]

if settings.DEBUG: # 개발 환경 에서만 사용s
    import debug_toolbar
    urlpatterns +=[
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)