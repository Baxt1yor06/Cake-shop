from django.urls import path
from .views import * 
urlpatterns = [
#  Base urls 
    path('', index, name='index'),
    path('about', about, name='about'),
    path('menu', menu, name='menu'),
    path('team', team, name='team'),
    path('service', service, name='service'),
    path('client', client, name='client'),
    path('contact', contact, name='contact'),

# Detail urls
    path('home1/<slug:home1>', detail1, name='detail1'),
    path('home3/<slug:home3>', detail2, name='detail2'),
    path('home4/<slug:home4>', detail3, name='detail3'),
    path('home5/<slug:home5>', detail4, name='detail4'),
    path('home6/<slug:home6>', detail5, name='detail5'),
    path('home7/<slug:home7>', detail6, name='detail6'),
    path('home8/<slug:home8>', detail7, name='detail7'),
    path('home9/<slug:home9>', detail8, name='detail8'),

# Change urls
    path('home1/update/<slug>/', Index_startUpdateView.as_view(), name='Index_startUpdateView'),
    path('home1/delete/<slug>/', Index_startDeleteView.as_view(), name='Index_startDeleteView'),
    path('home1/create/', Index_startCreateView.as_view(), name='Index_startCreateView'),
    path('home2/update/<slug>/', AboutUpdateView.as_view(), name='AboutUpdateView'),
    path('home2/delete/<slug>/', AboutDeleteView.as_view(), name='AboutDeleteView'),
    path('home2/create/', AboutCreateView.as_view(), name='AboutCreateView'),
    path('home3/update/<slug>/', BirthdayUpdateView.as_view(), name='BirthdayUpdateView'),
    path('home3/delete/<slug>/', BirthdayDeleteView.as_view(), name='BirthdayDeleteView'),
    path('home3/create/', BirthdayCreateView.as_view(), name='BirthdayCreateView'),
    path('home4/update/<slug>/', WeddingUpdateView.as_view(), name='WeddingUpdateView'),
    path('home4/delete/<slug>/', WeddingDeleteView.as_view(), name='WeddingDeleteView'),
    path('home4/create/', WeddingCreateView.as_view(), name='WeddingCreateView'),
    path('home5/update/<slug>/', CustomUpdateView.as_view(), name='CustomUpdateView'),
    path('home5/delete/<slug>/', CustomDeleteView.as_view(), name='CustomDeleteView'),
    path('home5/create/', CustomCreateView.as_view(), name='CustomCreateView'),
    path('home6/update/<slug>/', ServiceUpdateView.as_view(), name='ServiceUpdateView'),
    path('home6/delete/<slug>/', ServiceDeleteView.as_view(), name='ServiceDeleteView'),
    path('home6/create/', ServiceCreateView.as_view(), name='ServiceCreateView'),
    path('home7/update/<slug>/', TeamUpdateView.as_view(), name='TeamUpdateView'),
    path('home7/delete/<slug>/', TeamDeleteView.as_view(), name='TeamDeleteView'),
    path('home7/create/', TeamCreateView.as_view(), name='TeamCreateView'),
    path('home8/update/<slug>/', OfferUpdateView.as_view(), name='OfferUpdateView'),
    path('home8/delete/<slug>/', OfferDeleteView.as_view(), name='OfferDeleteView'),
    path('home8/create/', OfferCreateView.as_view(), name='OfferCreateView'),
    path('home9/update/<slug>/', ClientUpdateView.as_view(), name='ClientUpdateView'),
    path('home9/delete/<slug>/', ClientDeleteView.as_view(), name='ClientDeleteView'),
    path('home9/create/', ClientCreateView.as_view(), name='ClientCreateView'),







    ]
