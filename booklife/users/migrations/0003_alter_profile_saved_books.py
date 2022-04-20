# Generated by Django 3.2.6 on 2022-04-17 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0001_initial'),
        ('users', '0002_alter_profile_saved_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookshop.book'),
        ),
    ]
