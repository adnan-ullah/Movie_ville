# Generated by Django 3.2.5 on 2022-03-10 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image_all', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('headline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.news')),
            ],
        ),
    ]