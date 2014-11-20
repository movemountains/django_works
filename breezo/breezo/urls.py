from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'breezo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # authentication urls
      url(r'^login/', 'demo.views.login', name='login'),
      url(r'^authenticate/$', 'demo.views.authenticate', name='authenticate'),
      url(r'^logout/$', 'demo.views.logout', name='logout'),
      url(r'^login_success/$', 'demo.views.login_success', name='login_success'),
      url(r'^invalid/$', 'demo.views.invalid', name='invalid'),
    
    # registration urls
      url(r'^register/$', 'demo.views.register', name='register'),
      url(r'^register_success/$', 'demo.views.register_success', name='register_success'),

    # signup urls
     url(r'^signup/$', 'signup.views.signup', name='signup'),

    # user urls
   # url(r'^user/', include('user_profile.urls') namespace='user_profile'),    
    # breezo urls
     url(r'^breezo/$', 'demo.views.breezo', name='breezo'),
    #bucket urls
      url(r'^bucket/$', 'bucket.views.bucket', name="bucket"),
      url(r'^todo/$', 'bucket.views.todo', name='todo'),
      url(r'^done/$','bucket.views.done', name='done'),
      url(r'^doing/$','bucket.views.doing', name='doing'),

     
    # admin urls
      url(r'^admin/', include(admin.site.urls)),
)
