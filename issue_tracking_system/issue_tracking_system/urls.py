"""issue_tracking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

import authentication.views
import projects.views

router = routers.SimpleRouter()

router.register('projects', projects.views.ProjectViewSet, basename='projects')
router.register('create_project', projects.views.CreateProjectViewSet, basename='create_project')
router.register('project/<int:id>', projects.views.DetailProjectViewSet, basename='project')
router.register('update_project/<int:id>', projects.views.UpdateProjectViewSet, basename='update_project')
router.register('delete_project/<int:id>', projects.views.DeleteProjectViewSet, basename='delete_project')
router.register('project/<int:id>/add_contributor', projects.views.AddContributorViewSet, basename='add_contributor')
router.register('project/<int:id>/retrieve_contributors', projects.views.ListContributorViewSet,
                basename='retrieve_contributors')
router.register('project/<int:id>/delete_contributor/<int:id>', projects.views.DeleteContributorViewSet,
                basename='delete_contributor')
router.register('project/<int:id>/issues', projects.views.ListIssueViewSet, basename='issues')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', authentication.views.SignUpView.as_view(), name='sign_up'),
    path('api/', include(router.urls)),

]
