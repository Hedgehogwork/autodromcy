from django.conf.urls import include, url
from django.contrib import admin

from car.rest_views import CarList

urlpatterns = [
    # Examples:
    # url(r'^$', 'autodromcy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^cars_json/$',
        CarList.as_view(),
        name='car_list'
    ),
]
