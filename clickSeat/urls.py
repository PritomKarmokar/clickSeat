from django.contrib import admin
from django.urls import path

service_name = "clickSeat"
urlpatterns = [
    path(f'{service_name}/admin/', admin.site.urls),
]

#Admin
admin.site.site_header = "Click Movie Seat Service"
admin.site.index_title = "Click Movie Seat Service"
admin.site.site_site = "Click Movie Seat Service"