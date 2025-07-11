# Generated by Django 5.2.1 on 2025-07-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='profession',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
