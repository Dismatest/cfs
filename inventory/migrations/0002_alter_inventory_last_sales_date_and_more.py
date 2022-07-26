# Generated by Django 4.0.6 on 2022-11-26 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='last_sales_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='stock_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_received', models.IntegerField(default=1)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=19)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
    ]
