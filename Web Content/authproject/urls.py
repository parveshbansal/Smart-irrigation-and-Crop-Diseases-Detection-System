"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_page),
url(r'^weather/',views.weatherforcast),
url(r'^motor/',views.motor),
url(r'^irrigation/',views.irrigation1),
url(r'^detail/',views.detail),
url(r'^date/',views.date),
url(r'^croptype/',views.croptype),
url(r'^sowing/',views.sowing),
url(r'^accounts/',include('django.contrib.auth.urls')),
url(r'logout/',views.logout),
url(r'^signup/',views.signup),
url(r'^stop/',views.stop),
url(r'^godown1/',views.godown1),
url(r'^cropdetail/',views.godown,name='home'),
url(r'^delete/(?P<pk>\d+)/$',views.BeerDeleteView.as_view()),
url(r'^update/(?P<pk>\d+)/$',views.BeerUpdateView.as_view()),
]
