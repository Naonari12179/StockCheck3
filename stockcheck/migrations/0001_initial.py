# Generated by Django 3.1.3 on 2020-11-29 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='カテゴリー')),
            ],
            options={
                'verbose_name': 'カテゴリー',
                'verbose_name_plural': 'カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='飲料',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': '飲料',
                'verbose_name_plural': '飲料',
            },
        ),
        migrations.CreateModel(
            name='洋日配',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': '洋日配',
                'verbose_name_plural': '洋日配',
            },
        ),
        migrations.CreateModel(
            name='半生お菓子',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': '半生お菓子',
                'verbose_name_plural': '半生お菓子',
            },
        ),
        migrations.CreateModel(
            name='チーズ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': 'チーズ',
                'verbose_name_plural': 'チーズ',
            },
        ),
        migrations.CreateModel(
            name='お酒',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': 'お酒',
                'verbose_name_plural': 'お酒',
            },
        ),
        migrations.CreateModel(
            name='お菓子UZAWA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': 'お菓子UZAWA',
                'verbose_name_plural': 'お菓子UZAWA',
            },
        ),
        migrations.CreateModel(
            name='お菓子FUKUCHI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': 'お菓子FUKUCHI',
                'verbose_name_plural': 'お菓子FUKUCHI',
            },
        ),
        migrations.CreateModel(
            name='お菓子',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockcheck.categorys')),
            ],
            options={
                'verbose_name': 'お菓子',
                'verbose_name_plural': 'お菓子',
            },
        ),
    ]
