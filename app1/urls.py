from django.urls import path
from app1 import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.homev,name="homepage"),
    path('login',views.loginv,name="loginpage"),
    path('logout',views.logoutV,name="logoutpage"), 
    path('about',views.aboutv,name="aboutpage"),
    path('contact',views.contactv,name="contactpage"),
    path('event',views.eventv,name="eventpage"),
    path('club',views.clubv,name="clubpage"),
    path('nss',views.nssv,name="nsspage"),
    path('ncc',views.nccv,name="nccpage"),
    path('create',views.createv,name="createpage"),
    path('tm',views.toastmasterv,name="tmpage"),
    path('saro',views.sarov,name="saropage"),
    path('sb',views.shutterbugv,name="sbpage"),
    path('update/<int:rid>',views.update,name="updatepage"),
    path('delete/<int:rid>',views.delete,name='deletepage'),
    path('staff',views.staffv,name='staffpage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.ASSETS_URL, document_root=settings.ASSETS_ROOT)