# Generated by Django 3.2.3 on 2022-05-18 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('className', models.TextField(blank=True, help_text='className to wrap driver.js popover', null=True)),
                ('animate', models.BooleanField(default=True, help_text='Whether to animate or not')),
                ('opacity', models.FloatField(default=0.75, help_text='Background opacity (0 means only popovers and without overlay)')),
                ('padding', models.IntegerField(default=10, help_text='Distance of element from around the edges')),
                ('allowClose', models.BooleanField(default=True, help_text='Whether the click on overlay should close or not')),
                ('overlayClickNext', models.BooleanField(default=False, help_text='Whether the click on overlay should move next')),
                ('doneBtnText', models.CharField(blank=True, help_text='Text on the final button', max_length=200, null=True)),
                ('closeBtnText', models.CharField(blank=True, help_text='Text on the close button for this step', max_length=200, null=True)),
                ('stageBackground', models.CharField(blank=True, help_text='Background color for the staged behind highlighted element', max_length=200, null=True)),
                ('nextBtnText', models.CharField(blank=True, help_text='Next button text for this step', max_length=200, null=True)),
                ('prevBtnText', models.CharField(blank=True, help_text='Previous button text for this step', max_length=200, null=True)),
                ('showButtons', models.BooleanField(default=False, help_text='Do not show control buttons in footer')),
                ('keyboardControl', models.BooleanField(default=True, help_text='Allow controlling through keyboard (escape to close, arrow keys to move)')),
                ('scrollIntoViewOptions', models.TextField(blank=True, help_text='We use `scrollIntoView()` when possible, pass here the options for it if you want any - dictionary {}', null=True)),
                ('onHighlightStarted', models.TextField(blank=True, help_text='Called when element is about to be highlighted', null=True)),
                ('onHighlighted', models.TextField(blank=True, help_text='Called when element is fully highlighted', null=True)),
                ('onDeselected', models.TextField(blank=True, help_text='Called when element has been deselected', null=True)),
                ('onReset', models.TextField(blank=True, help_text='Called when overlay is about to be cleared', null=True)),
                ('onNext', models.TextField(blank=True, help_text='Called when moving to next step on any step', null=True)),
                ('onPrevious', models.TextField(blank=True, help_text='Called when moving to previous step on any step', null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='DriverStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_nbr', models.IntegerField()),
                ('element', models.TextField(help_text='Query selector string or Node to be highlighted')),
                ('stageBackground', models.TextField(blank=True, help_text='Background color for the staged behind highlighted element', null=True)),
                ('className', models.TextField(blank=True, help_text='className to wrap this specific step popover in addition to the general className in Driver options', null=True)),
                ('title', models.TextField(blank=True, help_text='Title on the popover', null=True)),
                ('description', models.TextField(blank=True, help_text='Body of the popover', null=True)),
                ('showButtons', models.BooleanField(default=False, help_text='Do not show control buttons in footer')),
                ('doneBtnText', models.CharField(blank=True, help_text='Text on the final button', max_length=200, null=True)),
                ('closeBtnText', models.CharField(blank=True, help_text='Text on the close button for this step', max_length=200, null=True)),
                ('nextBtnText', models.CharField(blank=True, help_text='Next button text for this step', max_length=200, null=True)),
                ('prevBtnText', models.CharField(blank=True, help_text='Previous button text for this step', max_length=200, null=True)),
                ('onNext', models.TextField(blank=True, help_text='Called when moving to next step from current step', null=True)),
                ('onPrevious', models.TextField(blank=True, help_text='Called when moving to previous step from current step', null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driversteps', to='Driverjs.driver')),
            ],
            options={
                'ordering': ('-step_nbr',),
                'unique_together': {('driver', 'step_nbr')},
            },
        ),
    ]