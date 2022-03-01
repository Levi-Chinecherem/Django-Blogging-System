# Generated by Django 4.0 on 2022-02-21 13:48

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
                ('title', models.CharField(max_length=200)),
                ('blog_slug', models.SlugField(max_length=200, unique=True)),
                ('desc1', models.TextField(max_length=400, verbose_name='Description One, Short Description')),
                ('desc2', models.TextField(blank=True, null=True, verbose_name='Description Two')),
                ('image1', models.ImageField(max_length=200, upload_to='images/posts')),
                ('brief', models.TextField(max_length=400, null=True, verbose_name='Subtitle or Selling Point')),
                ('desc3', models.TextField(blank=True, null=True, verbose_name='Description Three')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('comment_counter', models.IntegerField(null=True)),
                ('image2', models.ImageField(max_length=200, upload_to='images/uploads/% Y/% m/% d/')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]