from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Partner (models.Model):  # hamkorlar
    name = models.CharField(max_length=250, verbose_name='Name') # Translation
    image = models.ImageField(upload_to='./partner/', verbose_name='Image')
    url = models.URLField(verbose_name='Url')

    def __str__(self):
        return self.name


class Department(models.Model):  #Markazlar
    name = models.CharField(max_length=250, verbose_name='Markaz nomi') #Translation
    content = RichTextUploadingField(verbose_name='Content') #Translation

    sees = models.IntegerField(default=1, verbose_name="Kurilganlar")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Update time')

    def __str__(self):
        return self.name

class Employee(models.Model):   #markazlar ishchilari
    name = models.CharField(max_length=200, verbose_name='F.I.O')
    image = models.ImageField(default='./employee/avatar.png', upload_to='./employee', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone_number = models.CharField(max_length=50, verbose_name='Telefon')
    academic_title = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True) #Translation  --------

    is_chief = models.BooleanField(default=False)
    reception_time = RichTextUploadingField(null=True, blank=True) #Translation

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Rectory(models.Model):  # rektorat
    name = models.CharField(max_length=200, verbose_name='F.I.O')
    image = models.ImageField(upload_to='./rectory/', verbose_name='Image')
    content = RichTextUploadingField(verbose_name="Information") #Translation
    academic_title = models.CharField(max_length=200, verbose_name='Academic Title') #Translation  ------
    address = models.TextField(verbose_name='Address', null=True, blank=True) #Translation

    phone_number = models.CharField(max_length=50, verbose_name='Phone Number', null=True, blank=True)
    fax_number = models.CharField(max_length=50, verbose_name='Fax Number', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    facebook = models.CharField(max_length=100, verbose_name='Facebook', null=True, blank=True)
    instagram = models.CharField(max_length=100, verbose_name='Instagram', null=True, blank=True)
    telegram = models.CharField(max_length=100, verbose_name='Telegram', null=True, blank=True)

    is_rector = models.BooleanField(default=False)
    position = models.CharField(max_length=250, verbose_name='Position') #Translation ------
    reception_time = RichTextUploadingField(verbose_name='Qabul vaqti') #Translation

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    icon_class = models.CharField(max_length=250, verbose_name='Icon Name')
    url = models.URLField(verbose_name='Url')

    def __str__(self):
        return self.name


class Sahifalar(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = RichTextUploadingField(verbose_name='Content')
    page_name = models.CharField(max_length=255, verbose_name='Page url')

    def __str__(self):
        return self.page_name
