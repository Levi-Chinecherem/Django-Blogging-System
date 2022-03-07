from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import blog_view, home_view, blog_form_view, blog_details_view, comment_reply_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('blog/', blog_view, name = 'blog'),
    path('blog/post/', blog_form_view, name = 'blog_post_form'),
    path('blog/<slug:blog_slug>/', blog_details_view, name = 'blog_details'),
    path('comment/reply/', comment_reply_view, name = 'reply_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
