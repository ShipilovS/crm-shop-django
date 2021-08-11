# Generated by Django 3.2.5 on 2021-08-02 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm_app', '0003_auto_20210802_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='key_product_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='ForeignKeyUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='key_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.product', verbose_name='ForeignKey'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Инициалы'),
        ),
    ]
