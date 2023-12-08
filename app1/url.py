from app1.views import*
from django.url import path

app_name='yeswanth'

urlpattern=[
    path('yeswanth/',yeswanth,name='yeswanth.html')
]