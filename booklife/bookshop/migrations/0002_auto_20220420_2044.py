# Generated by Django 3.2.6 on 2022-04-20 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Undefined', max_length=150),
        ),
        migrations.AddField(
            model_name='book',
            name='book_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='descr',
            field=models.CharField(default=None, max_length=600),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookshop.book')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bookshop.book')),
            ],
        ),
    ]
