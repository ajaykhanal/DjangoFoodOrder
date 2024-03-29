# Generated by Django 4.1.7 on 2023-03-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='uploads/foods/'),
        ),
    ]
