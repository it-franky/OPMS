from django.contrib import admin
import xadmin

from .models import Passwd,ExpenseRecords,IncomeRecords
# Register your models here.

class PasswdAdmin(object):
    list_display = ['title', 'name', 'password', 'website','mark']
    search_fields = ['title', 'name', 'password', 'website','mark']
    list_filter = ['title', 'name', 'password', 'website','mark']


class ExpenseRecordsAdmin(object):
    list_display = ['trans_date', 'trans_bal', 'payment_way', 'remarks']
    search_fields = ['trans_date', 'trans_bal', 'payment_way', 'remarks']
    list_filter = ['trans_date', 'trans_bal', 'payment_way', 'remarks']


class IncomeRecordsAdmin(object):
    list_display = ['trans_date', 'trans_bal', 'income_resource']
    search_fields = ['trans_date', 'trans_bal', 'income_resource']
    list_filter = ['trans_date', 'trans_bal', 'income_resource']

xadmin.site.register(Passwd, PasswdAdmin)
xadmin.site.register(ExpenseRecords, ExpenseRecordsAdmin)
xadmin.site.register(IncomeRecords, IncomeRecordsAdmin)
