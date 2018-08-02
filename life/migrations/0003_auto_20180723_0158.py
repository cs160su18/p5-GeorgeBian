# Generated by Django 2.0.7 on 2018-07-23 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20180718_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reading_level', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Created')),
                ('summary', models.CharField(max_length=1000)),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='life.Kid')),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]