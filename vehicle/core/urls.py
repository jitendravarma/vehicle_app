from django.conf.urls import url
from django.contrib.auth import logout

from .views import (IndexView, LoginView, LogOutView, SignupView,
                    VehicleView, VehicleUpdateView, DeleteVehicle)

# app_name = 'core'


urlpatterns = [
    # for user authentication
    url(r'^login/$', LoginView.as_view(), name="login-view"),
    url(r'^signup/$', SignupView.as_view(), name="signup-view"),
    url(r'^logout/$', LogOutView.as_view(), name="logout-view"),

    url(r'^home/$', IndexView.as_view(), name="index-view"),
    url(r'^vehicle/$', VehicleView.as_view(), name="vehicle-view"),
    url(r'^vehicle/update/(?P<pk>.*)$', VehicleUpdateView.as_view(),
        name="vehicle-update-view"),
    url(r'^vehicle/delete/$', DeleteVehicle.as_view(),
        name="delete-vehicle"),
]
