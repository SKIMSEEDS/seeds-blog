from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.category_list, name='category_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),\
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^polhome/$', views.PolHomePageView.as_view(), name="polhome"),
    url(r'^envihome/$', views.EnviHomePageView.as_view(), name="envihome"),
    url(r'^socihome/$', views.SociHomePageView.as_view(), name="socihome"),
    url(r'^home/$', views.SeedsHomePageView.as_view(), name="Seeds_home"),
    url(r'^governmen/$', views.GovernmentPageView.as_view(), name='government'),
	url(r'^activism/$', views.ActivismPageView.as_view(), name='activism'),	
	url(r'^rights/$', views.RightsPageView.as_view(), name='rights'),
	url(r'^global_warming/$', views.GlobalWarmingPageView.as_view(), name='global_warming'),
	url(r'^animal_rights/$', views.AnimalRightsPageView.as_view(), name='animal_rights'),
	url(r'^other/$', views.OtherPageView.as_view(), name='other'),
	url(r'^LGBTQ/$', views.LGBTQPageView.as_view(), name='LGBTQ+'),
	url(r'^Health/$', views.HealthPageView.as_view(), name='Health'),
	url(r'^sociother/$', views.SociOtherPageView.as_view(), name='sociother'),
	url(r'^about_us/$', views.AboutUsPageView.as_view(), name='about_us'),
	url(r'^contact_us/$', views.ContactUsPageView.as_view(), name='contact_us'),
	url(r'^meet_the_team/$', views.MeetTheTeamPageView.as_view(), name='meet_the_team'),

]