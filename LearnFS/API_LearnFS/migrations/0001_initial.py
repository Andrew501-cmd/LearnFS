# Generated by Django 4.2.1 on 2023-05-25 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Заголовок')),
                ('summary', models.TextField(max_length=500, verbose_name='Описание')),
                ('html', models.TextField(verbose_name='HTML')),
                ('num_questions', models.CharField(max_length=2, verbose_name='Количество вопросов в тесте')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_edit', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=4, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20, verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Вопрос')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API_LearnFS.article', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API_LearnFS.group', verbose_name='Класс'),
        ),
        migrations.AddField(
            model_name='article',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API_LearnFS.subject', verbose_name='Предмет'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Вариант ответа')),
                ('isRight', models.BooleanField(verbose_name='Правильность')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API_LearnFS.questions', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
    ]
