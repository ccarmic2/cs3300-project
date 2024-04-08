from django.urls import path
from .views import (
    CalendarDatesListView,
    CalendarDatesDetailView,
    SupplyTaskDetailView,
    SupplyTaskListView,
    index,
    add_date,
    update_date,
    delete_date,
    add_supply,
    update_supply,
    delete_supply,
)

urlpatterns = [
    path("", index, name="index"),
    path("dates/", CalendarDatesListView.as_view(), name="dates"),
    path("dates/<int:pk>", CalendarDatesDetailView.as_view(), name="date-detail"),
    path("dates/add/", add_date, name="date-add"),
    path("dates/<int:pk>/update/", update_date, name="date-update"),
    path("dates/<int:pk>/delete/", delete_date, name="date-delete"),
    path("supplies/", SupplyTaskListView.as_view(), name="supplies"),
    path("supplies/<int:pk>", SupplyTaskDetailView.as_view(), name="supply-detail"),
    path("supplies/add/", add_supply, name="supply-add"),
    path("supplies/<int:pk>/update", update_supply, name="supply-update"),
    path("supplies/<int:pk>/update/", delete_supply, name="supply-delete"),
]
