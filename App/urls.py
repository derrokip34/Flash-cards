from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^new_flash_card',views.post_flash_card,name='newFlashCard'),
    url(r'^update_flash_card/(\d+)',views.update_flash_card,name='update'),
    url(r'^subject/cards/(\w+)/(\d+)$',views.subject_cards,name='subject'),
    url(r'^search/',views.search_flashcard,name='search'),
]
