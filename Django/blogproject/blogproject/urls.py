from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form 을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    
    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # detail 함수에 blog_id 라는 인수를 int 타입으로 넘김
    path('detail/<int:blog_id>', views.detail, name='detail'),

]

# media 파일에 접근할 수 있는 url도 추가해주어야 함, import static, settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)