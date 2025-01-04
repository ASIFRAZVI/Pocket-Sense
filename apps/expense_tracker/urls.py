from rest_framework.urls import path
from apps.expense_tracker.views import ExpenseView,get_total_expense

urlpatterns = [
    path('expense/', ExpenseView.as_view(), name='expense-add-get'),
    path('expense/<uuid:expense_id>/', ExpenseView.as_view(), name='expense-retrive-update-delete'),
    path('expense/total/', get_total_expense, name='get_total_expense'),
    path('expense/total/<uuid:catogary>/', get_total_expense, name='get_total_expense-by-catogary'),
]
