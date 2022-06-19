from django.urls import path

from .views import (
ArticleCreateView,
ArticleListView,
ArticleUpdateView,
ArticleDetailView,
ArticleDeleteView,
CommentCreateView, 
)




urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'), 
    
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), 
    
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
     
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    
    path('', ArticleListView.as_view(), name='article_list'),
]
