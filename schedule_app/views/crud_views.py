from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from schedule_app.decorators import allowed_users
from ..models import CalendarDates, SupplyTask
from ..forms import DateForm, SupplyForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_role'])
def add_date(request):
    form = DateForm()
        #handle a POST request to create a new project
    if request.method == 'POST':
        #copys the data from the POST request
        date_data = request.POST.copy()
        #sets the portfolio id for the new project
        form = DateForm(date_data)
        #check if valid
        if form.is_valid():
            #save the project to the data base and its association to 
            #the portfolio
            date = form.save(commit=False)
            date.save()
            print("created ", date)

            #redirect to the portfolio detail on success
            return redirect('dates')
    return render(request, "schedule_app/forms/add_date.html", {"form": form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_role'])
def update_date(request, pk):
    date = CalendarDates.objects.get(pk=pk)
    form = DateForm(request.POST or None, instance=date)
    #form data is either saved if POST or info is posted to text boxes
    
    if request.method == 'POST':
        #saves the changes made to the project in the database
        if form.is_valid():
            form.save()
            date.save()
            print("updated ", date)
            return redirect('date-detail', pk)
    return render(request, "schedule_app/forms/update_date.html", {"form": form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_role'])
def delete_date(request, pk):
    date = CalendarDates.objects.get(pk=pk)
    if request.method == "POST":
        date.delete()
        print("deleted ", date)
        return redirect('dates')
    return render(request, "schedule_app/forms/delete_date.html", {"date": date})


@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_role', 'cleaner_role'])
def add_supply(request):
    form = SupplyForm()
            #handle a POST request to create a new project
    if request.method == 'POST':
        #copys the data from the POST request
        supply_data = request.POST.copy()
        #sets the portfolio id for the new project
        form = SupplyForm(supply_data)
        #check if valid
        if form.is_valid():
            #save the project to the data base and its association to 
            #the portfolio
            supply = form.save(commit=False)
            supply.save()
            print("created ", supply)

            #redirect to the portfolio detail on success
            return redirect('supplies')
    return render(request, "schedule_app/forms/add_supply.html", {"form": form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_role', 'cleaner_role'])
def update_supply(request, pk):
    supply = SupplyTask.objects.get(pk=pk)
    form = SupplyForm(request.POST or None, instance=supply)
        #form data is either saved if POST or info is posted to text boxes
    
    if request.method == 'POST':
        #saves the changes made to the project in the database
        if form.is_valid():
            form.save()
            supply.save()
            print("updated ", supply)
            return redirect('supply-detail', pk)
    return render(request, "schedule_app/forms/update_supply.html", {"form": form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_role', 'cleaner_role'])
def delete_supply(request, pk):
    supply = SupplyTask.objects.get(pk=pk) 
    if request.method == "POST":
        supply.delete()
        print("deleted ", supply)
        return redirect('supplies')
    return render(request, "schedule_app/forms/delete_supply.html", {"supply": supply})
