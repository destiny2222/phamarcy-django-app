from django.urls import path
from index import views
from Study.views import tutorView
from account.views import *
from django.contrib.auth import views as auth_views


app_name = 'index'
urlpatterns = [
    path('', views.HomeView , name='home'),
    path('about/', views.AboutView, name='about'),
    path('login/', LoginView, name='login'),
    path('logout/', logout_View, name='logout'),
    path('profile', profileView, name='profile' ),
    path('register/', RegisterView, name='register'),
    path('dashboard/', dashboard_view, name='dashboard' ),
    path('other_user/<slug>/', other_user_profile, name='other_user'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blogdetails/<int:pk>', views.BlogDetailsView.as_view(), name='blog_details'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('categoryshop/<int:pk>', views.categoryshop_details.as_view(), name='shopcategory'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('course/', views.courseView.as_view(), name='course'),
    path('tutor/', tutorView, name='tutor'),
    # path('shopcategory/<int:pk>', categoryshop_details.as_view(), name='shopcategory'),
    path('information/', views.InformationView.as_view(), name='information'),
    path('excos/', views.ExcosView.as_view(), name='excos'),
    path('search', views.search, name="search"),
    path('coursefiles/<int:pk>/', views.UploadFileView.as_view(), name='coursedetails'),
    path('accommodation/', views.accommodationview.as_view(), name='accommodation'),
    path('pens/', views.PensView.as_view(), name='pen'),
    path('pendetails/<int:pk>', views.pans.as_view(), name='pendetails'),
    path('textbook/', views.textbook.as_view(), name='textbook'),
    path('study/<int:id>/', views.studyView.as_view(), name='study'),
    path('studydetails/<int:pk>/', views.studycategoryView.as_view(), name='studdetails'),
    path('success/', views.sucess.as_view(), name='success'),
]