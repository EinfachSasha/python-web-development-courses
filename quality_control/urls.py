from django.urls import path
from . import views
from .views import index, IndexView, bug_list, BugDetailView, feature_list, FeatureDetailView, add_bug_report, add_feature_request


app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('', index, name='index'),
    path('index_view/', IndexView.as_view(), name='index_view'),
    path('bugs/', bug_list, name='bug_list'),
    path('bugs/<int:pk>/', BugDetailView.as_view(), name='bug_detail'),
    path('features/', feature_list, name='feature_list'),
    path('features/<int:pk>/', FeatureDetailView.as_view(), name='feature_detail'),
    path('add_bug/', add_bug_report, name='add_bug_report'),
    path('add_feature/', add_feature_request, name='add_feature_request'),
]
