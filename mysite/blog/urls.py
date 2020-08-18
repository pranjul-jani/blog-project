from blog import views
from django.urls import path


url_patterns = [
    path('', views.ListView.as_view(), name='post_list'),
    path('post/new/<int:pk>', views.CreatePostView.as_view(), name='post_new'), # create
    path('post/<int:pk>', views.DetailView.as_view(), name='post_detail'), # retrieve
    path('post/<int:pk>/edit/', views.UpdateView.as_view(), name='post_edit'), # update
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'), # delete
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:id>/publish', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
    path('about/', views.AboutView.as_view(), name='about'),

]