from django.db import models

# Create your models here.

PASSWORD_TYPE = (('1', 'APP'), ('2', '网站'), ('3', '银行卡'), ('4', '信用卡'), ('5', '运维'))


class Passwd(models.Model):
    title = models.CharField(choices=PASSWORD_TYPE, max_length=2, default='1')
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    website = models.CharField(max_length=40, null=True, blank=True)
    mark = models.CharField(max_length=100)

    class Meta:
        verbose_name = "密码"
        verbose_name_plural = verbose_name


PAYMENT = (('1', '现金'), ('2', '支付宝'), ('3', '花呗'), ('4', '微信'), ('5', '京东白条'), ('6', '银行卡'), ('7', '信用卡'))
INCOME = (('1','现金'),('2','工资'),('3','公积金'),('4','医保'),('5','微信红包'))


class ExpenseRecords(models.Model):
    trans_date = models.DateField()
    trans_bal = models.FloatField()
    payment_way = models.CharField(choices=PAYMENT,max_length=10)
    remarks = models.CharField(max_length=50,verbose_name="备注")

    class Meta:
        verbose_name = "消费记录"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.remarks

class IncomeRecords(models.Model):
    trans_date= models.DateField()
    trans_bal = models.FloatField()
    income_resource = models.CharField(choices=INCOME,max_length=15)

    class Meta:
        verbose_name = "收入明细"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.income_resource


CLOSEFLAG = (('0','未结清'),('1','已结清'))


class LoanCreditDTL(models.Model):
    loan_date = models.DateField()
    loan_amount = models.FloatField()
    rate_amount = models.FloatField()
    loan_length = models.IntegerField(verbose_name="贷款期限（月数）")
    loan_balance = models.FloatField()
    close_flag = models.CharField(choices=CLOSEFLAG,max_length=10)
    loan_purpose = models.CharField(max_length=50,verbose_name="贷款用途")
    loan_begin_date = models.DateField()
    loan_end_date = models.DateField()

    class Meta:
        verbose_name = "消费记录"
        verbose_name_plural = verbose_name

