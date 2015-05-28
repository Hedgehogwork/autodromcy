from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from car.rest_views import CarList
from django.conf import settings
from django.contrib.staticfiles import views



urlpatterns = [
    # Examples:
    #url(r'^$', 'autodromcy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^cars_json/$',
        CarList.as_view(),
        name='car_list'
    ),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]
