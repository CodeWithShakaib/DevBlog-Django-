# Generated by Django 3.0.8 on 2020-07-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.TextField()),
                ('published_date', models.DateField()),
                ('time_read', models.CharField(choices=[('5', '5 min'), ('10', '10 min'), ('15', '15 min'), ('20', '20 min'), ('25', '25 min')], max_length=10)),
                ('content', models.TextField()),
            ],
        ),
    ]