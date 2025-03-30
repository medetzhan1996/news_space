from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'news'

urlpatterns =[
	path('',views.HomeView.as_view(), name='HomeView'),
	path('about/',views.AboutView.as_view(), name='about_view'),
	path('sholl/',views.ShollView.as_view(), name='sholl_view'),
	path('team/',views.TeamView.as_view(), name='team_view'),
	path('contact/',views.ContactView.as_view(), name='contact_view'),
	path('post/<int:id>/', views.PostDetailView.as_view(), name='post_detail'),
	path('post/list/', views.PostListView.as_view(), name='post_list'),
]