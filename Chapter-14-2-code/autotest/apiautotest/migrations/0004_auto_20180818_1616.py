# Generated by Django 2.0.5 on 2018-08-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiautotest', '0003_auto_20180818_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httpapi',
            name='requestBody',
            field=models.TextField(blank=True, max_length=2048, null=True, verbose_name='请求体'),
        ),
        migrations.AlterField(
            model_name='httpapi',
            name='requestHeader',
            field=models.TextField(blank=True, max_length=2048, null=True, verbose_name='请求header'),
        ),
        migrations.AlterField(
            model_name='httpapi',
            name='requestParameterType',
            field=models.CharField(blank=True, choices=[('form-data', '表单(form-data)'), ('raw', '原数据(raw)')], max_length=50, null=True, verbose_name='请求参数格式'),
        ),
    ]