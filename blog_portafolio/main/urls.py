from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    #path('contacto/', views.ContactView.as_view(), name='contacto'),
    #path('portafolio/', views.PortfolioView.as_view(), name='portfolio'),
    #path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='portfolioDetail'),
    #path('blog1/', views.BlogView.as_view(), name='blogs'),
    #path('blog2/<slug:slug>', views.BlogDetailView.as_view(), name='blog2')
]