from django.db import models
class Company(models.Model):
    name = models.CharField(max_length=30,verbose_name='نام شرکت')
    slug = models.SlugField(max_length=100,allow_unicode=True,verbose_name='آدرس اینترنتی شرکت')
    about = models.TextField(verbose_name='درباره شرکت')
    cover = models.ImageField(upload_to='media',verbose_name='عکس شرکت')
    founder = models.OneToOneField('account.User',on_delete=models.CASCADE,verbose_name='سازنده',related_name='Fcompany')
    staff = models.ManyToManyField('staff.Staff',verbose_name='کارکنان',related_name='Scompany')
    created = models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True,verbose_name='به روز شده')

    def __str__(self):
        return  self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'
