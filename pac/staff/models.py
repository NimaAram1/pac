from django.db import models

class Staff(models.Model):
    STAFF_CHOICES = (
        ('staf','کارمند'),
        ('send','مدیر محصول'),
        ('plan','حسابدار'),
    )
    first_name = models.CharField(max_length=15,verbose_name='نام')
    last_name = models.CharField(max_length=15,verbose_name='نام خانوادگی')
    user = models.OneToOneField('account.User',on_delete=models.CASCADE,verbose_name='کاربر',related_name='Ustaff')
    profile_image = models.ImageField(upload_to='media',verbose_name='عکس پروفایل',blank=True,null=True)
    bio = models.TextField(verbose_name='درباره کارمند',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True, verbose_name='به روز شده')
    job = models.CharField(max_length=4,choices=STAFF_CHOICES,verbose_name='سمت')
    resume = models.FileField(blank=True,null=True,verbose_name='رزومه',upload_to='resume')

    def __str__(self):
        return  self.name

    class Meta:
        ordering = ['last_name']
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'
