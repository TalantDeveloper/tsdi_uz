from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Chair(models.Model):  #Kafedralar
    name = models.CharField(max_length=255, verbose_name='Kafedra nomi') #translation
    sub_name = models.CharField(max_length=100, verbose_name='Subdomain nomi')
    content = RichTextUploadingField(null=True, blank=True, verbose_name='Kafedra haqida') #translation

    def __str__(self):
        return self.name


class New(models.Model):  #Yangiliklar
    title = models.CharField(max_length=255, verbose_name='Yangiliklar') #Translation
    image = models.ImageField(upload_to='./news/', default='/news/news.png')
    chair = models.ManyToManyField(Chair, blank=True, verbose_name='Kafedra news')
    content = RichTextUploadingField(null=True, blank=True, verbose_name='Yangilik haqida') #translation
    sees = models.IntegerField(default=1)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def see_add(self):
        self.sees = self.sees + 1
        self.save()

    def __str__(self):
        return self.title


class TeacherChair(models.Model):  #Kafedra o'qituvchilari
    name = models.CharField(max_length=150, verbose_name='Ism Familya')
    chair = models.ForeignKey(Chair, verbose_name='kafedra name', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='./kafedra/', default='./kafedra/avatar.png', verbose_name='Rasm Ustoz')

    position = models.TextField(verbose_name='Ustoz haqida', null=True, blank=True) #tranlation
    academic_title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Ustoz darajasi') #translation

    phone_num = models.CharField(max_length=200, verbose_name='Telefon nomer')
    email = models.CharField(max_length=200, verbose_name='Ustoz Email')

    def __str__(self):
        return self.name


class Faculty(models.Model): #Fakultet
    name = models.CharField(max_length=250, verbose_name='Fakultet nomi')  #Translation
    sub_name = models.CharField(max_length=250, verbose_name='Fakultet_name', null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Fakultet haqida')  #Translation
    kafedra = models.ManyToManyField(Chair, verbose_name='kafedralar')

    def __str__(self):
        return self.name


class TeacherFaculty(models.Model): #fakultet dekanlar
    name = models.CharField(max_length=250, verbose_name='Ustoz ismi')
    image = models.ImageField(upload_to='./fakultet/', default='/fakultet/avatar.png')
    fakultet = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    academic_title = models.TextField(null=True, blank=True, verbose_name='Academic title') # Translation

    phone_number = models.CharField(max_length=250, null=True, blank=True, verbose_name='Telefon nomer')
    email = models.EmailField(max_length=200, verbose_name='Email', null=True, blank=True)
    reception_time = RichTextUploadingField(null=True, blank=True, verbose_name='Qabul vaqti')

    position = models.CharField(max_length=250, verbose_name='Position', null=True, blank=True)
    is_dean = models.BooleanField(default=False, verbose_name='Dekanmi?')

    def __str__(self):
        return self.name
