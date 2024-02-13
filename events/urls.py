app_name = "events"

from django.urls import path
from .views import *


urlpatterns=[
    # my evnts
    path("events/" , my_events , name="my-events"),
    path("add-event/" , add_event , name="add-event"),
    path("update-event/<int:pk>/" , update_event , name="update-event"),

    # other events
    path("other-events/" , other_events , name="other-events"),
    path("event-view/<int:pk>/" , event_view , name="event-view"),
    path("paticipents-view/<int:pk>/" , paticipents_view , name="paticipents-view"),

    path("api/event-registration/" , event_registration , name="event-registration"),
    
]