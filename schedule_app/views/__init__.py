from .account_views import (
    registerPage, 
    loginPage, 
    logoutPage,
    )
from .crud_views import (
    add_date, 
    add_supply, 
    update_date, 
    update_supply, 
    delete_date, 
    delete_supply,
    )
from .display_views import (
    CalendarDatesDetailView, 
    CalendarDatesListView, 
    SupplyTaskDetailView, 
    SupplyTaskListView, 
    index,
    )