from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'breezo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # authentication urls
      url(r'^breezo_login/', 'demo.views.breezo_login', name='breezo_login'),
      url(r'^authenticate/$', 'demo.views.authenticate', name='authenticate'),
      url(r'^breezo_logout/$', 'demo.views.breezo_logout', name='breezo_logout'),
      url(r'^breezo_loginsuccess/$', 'demo.views.breezo_loginsuccess', name='breezo_loginsuccess'),
      url(r'^breezo_loginfail/$', 'demo.views.breezo_loginfail', name='breezo_loginfail'),
    
    # registration urls
      url(r'^breezo_register/$', 'demo.views.breezo_register', name='breezo_register'),
      url(r'^breezo_registersuccess/$', 'demo.views.breezo_registersuccess', name='breezo_registersuccess'),

    # signup urls
     url(r'^breezo_signup/$', 'signup.views.breezo_signup', name='breezo_signup'),

    # user urls
    # url(r'^user/', include('user_profile.urls') namespace='user_profile'),    
    # breezo urls
     url(r'^breezo_contact/$', 'demo.views.breezo_contact', name='breezo_contact'),
    #bucket urls
      url(r'^bucket/$', 'bucket.views.bucket', name="bucket"),
      url(r'^todo/$', 'bucket.views.todo', name='todo'),
      url(r'^done/$','bucket.views.done', name='done'),
      url(r'^doing/$','bucket.views.doing', name='doing'),

     
    # admin urls
      url(r'^admin/', include(admin.site.urls)),
)
