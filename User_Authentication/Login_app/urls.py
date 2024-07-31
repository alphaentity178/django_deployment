from django.urls import path
from Login_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 


app_name = 'Login_app'

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('register/' , views.register , name = 'register'),
    path('login/' , views.login_page , name = 'login_page'),
    path('user_login/' , views.user_login , name = 'user_login'),
    path('user_logout' , views.user_logout , name = 'user_logout')
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL , documet_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
