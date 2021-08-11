# Generated by Django 3.2.6 on 2021-08-11 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0006_auto_20210810_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default=1, max_length=20, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='categories_foregin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.categories', verbose_name='Название категории'),
        ),
    ]
