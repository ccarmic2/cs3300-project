from django.shortcuts import render
from django.views import generic
from datetime import datetime
import calendar
from ..utils import get_cal, get_day_num, get_link_args, get_occupied_days, check_month
#from schedule_app.decorators import unauthenticated_user
from ..models import CalendarDates, SupplyTask

# Create your views here.
class CalendarDatesListView(generic.ListView):
    model = CalendarDates


class SupplyTaskListView(generic.ListView):
    model = SupplyTask


class CalendarDatesDetailView(generic.DetailView):
    model = CalendarDates


class SupplyTaskDetailView(generic.DetailView):
    model = SupplyTask

def index(request, year=datetime.now().year, month=datetime.now().month):
    tasks = SupplyTask.objects.all()
    dates = CalendarDates.objects.all()
    first_day = get_day_num(datetime(year, month, 1).strftime("%A"))
    days_in_month = calendar.monthrange(year, month)[1]
    days_in_month = list(range(1, days_in_month+1))
    month_name = datetime(year, month, 1).strftime("%B")
    arg_dic = get_link_args(month, year)
    month = check_month(month)
    colored_days = get_occupied_days(days_in_month, dates, month)
    cal = get_cal(days_in_month, colored_days, first_day)
    context = {
               'tasks': tasks,
               'month': month_name,
               'year': year,
               'arg_dic':arg_dic,
               'cal': cal}
    print(context)
    return render(request, "schedule_app/index.html", context)