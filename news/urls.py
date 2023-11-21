from django.urls import path
from .views import NewsList, PostList


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', PostList.as_view()),
]