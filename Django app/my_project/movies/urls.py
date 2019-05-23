from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view()),
    #path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('movies/<int:pk>/', views.MovieDetailView.as_view()),
    path('autocomplete', views.Auto_complete_View.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
