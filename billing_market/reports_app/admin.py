from django.contrib import admin
from .models import Expenses, ExpensesDetails


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expenses_id', 'expenses_total_cost', 'expenses_date')


@admin.register(ExpensesDetails)
class ExpensesDetailsAdmin(admin.ModelAdmin):
    list_display = ('expenses_details_id', 'expenses_for', 'expenses_cost', 'expenses')
