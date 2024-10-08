from django.urls import path
from main.views import show_main, create_sneakers, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_sneakers, delete_sneakers, add_sneakers_entry_ajax




app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-sneakers', create_sneakers, name='create_sneakers'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-sneakers/<uuid:id>', edit_sneakers, name='edit_sneakers'),
    path('delete/<uuid:id>', delete_sneakers, name='delete_sneakers'),
    path('create-ajax', add_sneakers_entry_ajax, name='add_sneakers_entry_ajax'),
]