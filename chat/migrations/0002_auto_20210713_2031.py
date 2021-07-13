# Generated by Django 3.2.4 on 2021-07-13 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_token'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatlog',
            name='dst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_dst', to='users.user'),
        ),
        migrations.AlterField(
            model_name='chatlog',
            name='src',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_src', to='users.user'),
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1300)),
                ('dst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_dst', to='users.user')),
                ('src', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_src', to='users.user')),
            ],
        ),
    ]
