# Generated by Django 3.2.6 on 2021-10-08 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempocomentario', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Usuarios.user')),
            ],
            options={
                'ordering': ['-tiempocomentario'],
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(blank=True, max_length=200, null=True)),
                ('UserName', models.CharField(blank=True, max_length=200, null=True)),
                ('BirthDay', models.DateField(blank=True, null=True)),
                ('Avatar', models.ImageField(default='avatarusuario.png', upload_to='')),
                ('IsMusician', models.BooleanField(default=False)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.user')),
            ],
        ),
    ]
