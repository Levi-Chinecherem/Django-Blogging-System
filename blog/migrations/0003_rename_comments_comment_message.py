# Generated by Django 4.0 on 2022-02-23 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_comment_counter_alter_blog_blog_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='message',
        ),
    ]
