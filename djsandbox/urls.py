"""
URL configuration for djsandbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

import time

from django.contrib import admin
from django.http import HttpResponse, StreamingHttpResponse
from django.urls import path


def index(_):
    return HttpResponse("Hello, world. This gets updated!")


def streaming(_):
    def generate():
        for i in range(3):
            time.sleep(1)
            yield f"Response {i}\n\n"

    return StreamingHttpResponse(generate(), content_type="text/event-stream")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("streaming/", streaming),
    path("", index),
]
