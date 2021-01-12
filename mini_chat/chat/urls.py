from django.conf.urls import  url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import LoginView, LogoutView
from mini_chat import settings
from django.conf.urls.static import static

from chat.views import Register,Chat
urlpatterns = [
    url(r"^demo/$", Register.as_view(), name='register'),
    url(r"^chat/$", Chat.as_view(), name='chat'),
    url(r'login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'login/', LogoutView.as_view(template_name='logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
