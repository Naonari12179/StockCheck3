from django.db import models

# Create your models here.
import datetime
from datetime import  timedelta
from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone

# Create your models here.
class Categorys(models.Model):
    title = models.CharField('カテゴリー', max_length = 200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'
        
class お菓子UZAWA(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=21)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=14)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お菓子UZAWA'
        verbose_name_plural = 'お菓子UZAWA'
class お菓子FUKUCHI(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=21)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=14)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お菓子FUKUCHI'
        verbose_name_plural = 'お菓子FUKUCHI'

class お菓子(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=21)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=14)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お菓子'
        verbose_name_plural = 'お菓子'
class 半生お菓子(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=10)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=7)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=3)
        return sale3.date()
    class Meta:
        verbose_name = '半生お菓子'
        verbose_name_plural = '半生お菓子'
class 洋日配(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=5)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=2)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=1)
        return sale3.date()
    class Meta:
        verbose_name = '洋日配'
        verbose_name_plural = '洋日配'
class チーズ(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=7)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=3)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=1)
        return sale3.date()
    class Meta:
        verbose_name = 'チーズ'
        verbose_name_plural = 'チーズ'
class 飲料(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=14)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=7)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=3)
        return sale3.date()
    class Meta:
        verbose_name = '飲料'
        verbose_name_plural = '飲料'

class お酒(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - relativedelta(months=1)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=17)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お酒'
        verbose_name_plural = 'お酒'