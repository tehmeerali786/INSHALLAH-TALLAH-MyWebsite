from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views




urlpatterns = [

path('', include('django.contrib.auth.urls')),
path('', views.frontpage, name='frontpage'),
path('about/', views.about, name='about'),
path('we_do/', views.we_do, name='we_do'),
path('portfolio/', views.portfolio, name='portfolio'),
path('aiagents/', views.llm_based_ai_agents, name='aiagents'),
path('chatbots/', views.basic_ai_enabled_chatbots, name='chatbots'),
path('dlnlp/', views.deep_learning_nlp, name='dlnlp'),
path('waid/', views.web_development, name='waid'),
path('contact/', views.contact, name='contact'),


]


