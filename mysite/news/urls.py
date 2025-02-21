from django.urls import path, include, re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    

    
    #/the-thao.html
    
    #path('article/<slug:article_slug>',views.article, name="article"),

    re_path(r'^(?P<article_slug>[\w-]+)-a(?P<article_id>\d+)\.html$',views.article, name="article"),
    #/vai-nghin-dong-mot-kg-cam-sanh-a11.html

    #path('feed/<slug:feed_slug>',views.feed, name="feed"),

    re_path(r'^tin-tong-hop-(?P<feed_slug>[\w-]+)\.html$',views.feed, name="feed"),
    #/tin-tong-hop-vnexpress.html

    path('search.html',views.search, name="search"), 
    path('about.html',views.about, name="about.html"), 
    path('contact.html',views.contact, name="contact"), 
    re_path(r'^(?P<category_slug>[\w-]+)\.html$',views.category, name="category"),

    path('tinymce/', include('tinymce.urls'))
    #path('<slug:category_slug>',views.category, name="category"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)