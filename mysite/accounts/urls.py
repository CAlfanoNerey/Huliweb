from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import SignUpView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('items/', views.item_list, name='items'),
    path('checkout/', views.checkoutPage, name='checkoutPage'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='productPage'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('register/', SignUpView.as_view(), name='register_url'),
    path('login/', views.loginview, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('<int:pk>/profile/', views.ViewProfile.as_view(), name='view_profile'),
    path('requesterupdate/', views.edit_profile, name='requester_update'),
    path('password/', views.edit_password, name='password'),

    #path('<int:pk>/viewdoc/', views.viewdoc, name='viewdoc')

    # path(
    #     'login/',
    #     LoginView.as_view(
    #         template_name="login.html",
    #         authentication_form=UserLoginForm
    #         ),
    #     name='login'
    # ),
]
