from django.conf.urls import  url
from rest_framework.authtoken import views as tokenview
from rest_framework.urlpatterns import format_suffix_patterns
from food import views
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^estimate/$', views.CaloireEstimate.as_view()),
    url(r'^profile/$', views.UserPro.as_view()),
    url(r'^food/$', views.FoodCalorie.as_view()), 
    url(r'^users/$', views.UserList.as_view()),
    url(r'^register/$', views.CreateUserView.as_view()),
    # url(r'^addimage/$', views.AddImage.as_view()),
    # url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),   
    # url(r'^getimage/$', views.RetrieveImagesSecure.as_view()),
    # url(r'^getimageurl/$', views.RetrieveImages.as_view()),
    # url(r'^register/$', views.CreateUserView.as_view()),
    # url(r'^fileupload/$', views.AddImageNoToken.as_view()),
 
]



urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]