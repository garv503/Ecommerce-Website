# Generated by Django 4.2.3 on 2023-10-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_alter_drum_image_alter_keyboard_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
