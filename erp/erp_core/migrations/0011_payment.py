# Generated by Django 4.0.2 on 2022-06-28 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_core', '0010_alter_company_options_alter_invoice_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('ACTIVE', 'Active'), ('PASSIVE', 'Passive')], default='ACTIVE', max_length=10)),
                ('date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_receiver', to='erp_core.company')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_sender', to='erp_core.company')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
