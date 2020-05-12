# Generated by Django 3.0.6 on 2020-05-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'applicant'), (2, 'test candidate'), (3, 'successful candidate'), (4, 'employee'), (5, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ManyToManyField(to='accounts.EmployeeStatus'),
        ),
    ]