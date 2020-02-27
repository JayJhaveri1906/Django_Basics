from django.urls import path
from . import views
# . means yehi directory mae views naam ka file hai usse import kar.
urlpatterns = [path('',views.index,name="index")]
