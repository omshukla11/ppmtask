# Generated by Django 4.0.4 on 2022-05-16 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('aadhar_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('yearofpassing', models.PositiveIntegerField()),
                ('percentage', models.PositiveIntegerField()),
                ('aadhar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aadhar.aadhar')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('post_code', models.CharField(max_length=6)),
                ('aadhar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aadhar.aadhar')),
            ],
        ),
    ]
