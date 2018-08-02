from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name="index"),
    path('kids/', views.kids, name='kids'),
    path('admin/', admin.site.urls),
    path('life/', include('life.urls'))
]
