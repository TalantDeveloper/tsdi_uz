# Generated by Django 4.2.1 on 2023-06-21 10:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kafedra nomi')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Kafedra nomi')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Kafedra nomi')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Kafedra nomi')),
                ('sub_name', models.CharField(max_length=100, verbose_name='Subdomain nomi')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Kafedra haqida')),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Kafedra haqida')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Kafedra haqida')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Kafedra haqida')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Fakultet nomi')),
                ('name_uz', models.CharField(max_length=250, null=True, verbose_name='Fakultet nomi')),
                ('name_en', models.CharField(max_length=250, null=True, verbose_name='Fakultet nomi')),
                ('name_ru', models.CharField(max_length=250, null=True, verbose_name='Fakultet nomi')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Fakultet haqida')),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Fakultet haqida')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Fakultet haqida')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Fakultet haqida')),
                ('kafedra', models.ManyToManyField(to='fakultet.chair', verbose_name='kafedralar')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ustoz ismi')),
                ('image', models.ImageField(default='/fakultet/avatar.png', upload_to='./fakultet/')),
                ('academic_title', models.TextField(blank=True, null=True, verbose_name='Academic title')),
                ('academic_title_uz', models.TextField(blank=True, null=True, verbose_name='Academic title')),
                ('academic_title_en', models.TextField(blank=True, null=True, verbose_name='Academic title')),
                ('academic_title_ru', models.TextField(blank=True, null=True, verbose_name='Academic title')),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True, verbose_name='Telefon nomer')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('reception_time', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Qabul vaqti')),
                ('reception_time_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Qabul vaqti')),
                ('reception_time_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Qabul vaqti')),
                ('reception_time_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Qabul vaqti')),
                ('position', models.CharField(blank=True, max_length=250, null=True, verbose_name='Position')),
                ('position_uz', models.CharField(blank=True, max_length=250, null=True, verbose_name='Position')),
                ('position_en', models.CharField(blank=True, max_length=250, null=True, verbose_name='Position')),
                ('position_ru', models.CharField(blank=True, max_length=250, null=True, verbose_name='Position')),
                ('is_dean', models.BooleanField(default=False, verbose_name='Dekanmi?')),
                ('fakultet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fakultet.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherChair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ism Familya')),
                ('image', models.ImageField(default='./kafedra/avatar.png', upload_to='./kafedra/', verbose_name='Rasm Ustoz')),
                ('position', models.TextField(blank=True, null=True, verbose_name='Ustoz haqida')),
                ('position_uz', models.TextField(blank=True, null=True, verbose_name='Ustoz haqida')),
                ('position_en', models.TextField(blank=True, null=True, verbose_name='Ustoz haqida')),
                ('position_ru', models.TextField(blank=True, null=True, verbose_name='Ustoz haqida')),
                ('academic_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ustoz darajasi')),
                ('academic_title_uz', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ustoz darajasi')),
                ('academic_title_en', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ustoz darajasi')),
                ('academic_title_ru', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ustoz darajasi')),
                ('phone_num', models.CharField(max_length=200, verbose_name='Telefon nomer')),
                ('email', models.CharField(max_length=200, verbose_name='Ustoz Email')),
                ('chair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fakultet.chair', verbose_name='kafedra name')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Yangiliklar')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Yangiliklar')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Yangiliklar')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Yangiliklar')),
                ('image', models.ImageField(default='/news/news.png', upload_to='./news/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Yangilik haqida')),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Yangilik haqida')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Yangilik haqida')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Yangilik haqida')),
                ('sees', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('chair', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fakultet.chair', verbose_name='Kafedra news')),
            ],
        ),
    ]
