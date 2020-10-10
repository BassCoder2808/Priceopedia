# Generated by Django 3.1.1 on 2020-10-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('number_of_users_bought', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.category')),
            ],
        ),
    ]
