# Generated by Django 4.0.2 on 2023-07-16 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AimDealer',
            fields=[
                ('account', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], max_length=10)),
                ('dealer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dealer_name', models.CharField(max_length=200, null=True)),
                ('site_url', models.CharField(max_length=200, null=True)),
                ('account_manager', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webprovider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TargetSite',
            fields=[
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Pending', 'Pending'), ('Failed', 'Failed')], default='Pending', max_length=10)),
                ('entry_code', models.CharField(blank=True, default='', max_length=20, verbose_name='entry#')),
                ('site_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='site id (domain)')),
                ('site_url', models.CharField(blank=True, max_length=200, null=True)),
                ('web_provider', models.CharField(blank=True, max_length=50, null=True)),
                ('feed_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='feed#')),
                ('spider', models.CharField(max_length=50, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('condition', models.BooleanField()),
                ('unit', models.BooleanField()),
                ('year', models.BooleanField()),
                ('make', models.BooleanField()),
                ('model', models.BooleanField()),
                ('trim', models.BooleanField()),
                ('stock_number', models.BooleanField()),
                ('vin', models.BooleanField()),
                ('vehicle_url', models.BooleanField()),
                ('msrp', models.BooleanField()),
                ('price', models.BooleanField()),
                ('selling_price', models.BooleanField()),
                ('rebate', models.BooleanField()),
                ('discount', models.BooleanField()),
                ('images', models.BooleanField()),
                ('images_count', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='project.project')),
                ('site_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.aimdealer')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpiderLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spider_name', models.CharField(max_length=50, null=True)),
                ('allowed_domain', models.CharField(max_length=50, null=True)),
                ('items_scraped', models.CharField(max_length=50, null=True)),
                ('items_dropped', models.CharField(max_length=50, null=True)),
                ('finish_reason', models.CharField(max_length=50, null=True)),
                ('request_count', models.CharField(max_length=50, null=True)),
                ('status_count_200', models.CharField(max_length=50, null=True)),
                ('start_timestamp', models.CharField(max_length=50, null=True)),
                ('end_timestamp', models.CharField(max_length=50, null=True)),
                ('elapsed_time', models.CharField(max_length=50, null=True)),
                ('elapsed_time_seconds', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('target_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spider_logs', to='project.targetsite')),
            ],
        ),
        migrations.CreateModel(
            name='Scrape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spider', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('unit', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
                ('make', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('trim', models.CharField(blank=True, max_length=200, null=True)),
                ('stock_number', models.CharField(blank=True, max_length=50, null=True)),
                ('vin', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_url', models.CharField(blank=True, max_length=255, null=True)),
                ('msrp', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('selling_price', models.CharField(blank=True, max_length=50, null=True)),
                ('rebate', models.CharField(blank=True, max_length=50, null=True)),
                ('discount', models.CharField(blank=True, max_length=50, null=True)),
                ('image_urls', models.TextField(blank=True, null=True)),
                ('images_count', models.CharField(blank=True, max_length=50, null=True)),
                ('page', models.CharField(blank=True, max_length=50, null=True)),
                ('last_checked', models.DateTimeField(auto_now_add=True, null=True)),
                ('target_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scrapes', to='project.targetsite')),
            ],
        ),
        migrations.AddField(
            model_name='aimdealer',
            name='web_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='web_provider', to='project.webprovider'),
        ),
    ]
