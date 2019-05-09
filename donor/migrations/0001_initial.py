# Generated by Django 2.2 on 2019-05-09 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cnn_name', models.CharField(blank=True, max_length=255, null=True)),
                ('cnn_employer', models.CharField(blank=True, max_length=255, null=True)),
                ('cnn_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('cnn_note', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('contribution_total_2018', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('contribution_total_2020', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
