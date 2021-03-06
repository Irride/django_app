"""landing_page_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from core.views import landing_page_view
from core.views import landing_page_view_about
from core.views import contact_us_view
from core.views import feedbacks_view
from core.views import subjects_view, subject_item_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view),
    path('about/', landing_page_view_about),
    path('contact-us/', contact_us_view),
    path('feedbacks/', feedbacks_view, name = "feedbacks" ),
    path('subjects/', subjects_view, name = "subjects" ),
    path('subjects/<str:subject_name>/', subject_item_view, name = "subject")
    #path('feedbacks-bla/', feedbacks_view, name = "feedbacks")
]
