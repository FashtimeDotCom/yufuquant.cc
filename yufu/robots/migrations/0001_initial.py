# Generated by Django 3.0.7 on 2020-06-28 09:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_cryptography.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('pair', models.CharField(max_length=15, verbose_name='交易对')),
                ('margin_currency', models.CharField(max_length=10, verbose_name='保证金币种')),
                ('enabled', models.BooleanField(default=True, verbose_name='启用')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='启动时间')),
                ('ping_time', models.DateTimeField(blank=True, null=True, verbose_name='心跳时间')),
                ('order_sync_ts', models.BigIntegerField(blank=True, null=True, verbose_name='订单同步时间戳')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='创建于')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='修改于')),
                ('stream_key', django_cryptography.fields.encrypt(models.CharField(max_length=300, verbose_name='stream key'))),
                ('credential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robots', to='credentials.Credential', verbose_name='交易所凭证')),
            ],
            options={
                'verbose_name': '机器人',
                'verbose_name_plural': '机器人',
            },
        ),
    ]