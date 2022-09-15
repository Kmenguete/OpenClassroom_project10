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
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

import authentication.views
import projects.views

projects_router = routers.SimpleRouter(trailing_slash=False)
projects_router.register(r'project/?', projects.views.ProjectViewSet, basename="project")
# detail_project_router = routers.NestedSimpleRouter(projects_router, r'project/?', lookup="project")
# detail_project_router.register(r'project/?', projects.views.DetailProjectViewSet,
# basename="project")
users_router = routers.NestedSimpleRouter(projects_router, r'project/?', lookup="project")
users_router.register(r'users/?', projects.views.ContributorViewSet, basename="users")
issues_router = routers.NestedSimpleRouter(projects_router, r'project/?', lookup="project")
issues_router.register(r'issues/?', projects.views.IssueViewSet, basename="issues")
comments_router = routers.NestedSimpleRouter(issues_router, r'issues/?', lookup="issues")
comments_router.register(r'comments/?', projects.views.CommentViewSet, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', authentication.views.SignUpView.as_view(), name='sign_up'),
    path('', include(projects_router.urls)),
    # path('', include(detail_project_router.urls)),
    path('', include(users_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(comments_router.urls)),

]
