from django.contrib import admin
from django.urls import path

import predictor.views

urlpatterns = [
    path('', predictor.views.render_upload_page, name = 'upload'),
    path('history/', predictor.views.show_history, name = 'history')
]