# Generated by Django 3.2.25 on 2024-04-24 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0033_auto_20240125_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='cash_in_hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_adjust', models.TextField(max_length=100)),
                ('cash_cash', models.IntegerField(blank=True, null=True)),
                ('cash_description', models.TextField(max_length=100)),
                ('cash_date', models.DateField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.CreateModel(
            name='cashinhandTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=20)),
                ('transactiondate', models.DateField(auto_now=True)),
                ('cash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.cash_in_hand')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
    ]
