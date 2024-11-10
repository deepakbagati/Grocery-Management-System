# Generated by Django 4.1.5 on 2023-03-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryproducts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='category_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='category_images/'),
        ),
    ]
