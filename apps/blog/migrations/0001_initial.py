# Generated by Django 5.0.7 on 2024-07-30 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Sarlavhasi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mazmuni')),
                ('is_seen', models.IntegerField(default=0, verbose_name="Ko'rilganlar soni")),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Bloglar',
                'db_table': 'blog',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Kategoriya nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name="Rasm qo'yish")),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogImage', to='blog.blog')),
            ],
            options={
                'verbose_name': 'Blog Rasmlar',
                'verbose_name_plural': 'Blog Rasmlar',
                'db_table': 'blog_image',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='Category', to='blog.categories', verbose_name='Kategoriyasi'),
        ),
    ]
