from django.db import migrations


def create_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    custom_domain = "tst-3c44f02b-3ef0-41f-125.botics.io"

    site_params = {
        "name": "TST-3c44f02b-3ef0-41fd-9",
    }
    if custom_domain:
        site_params["domain"] = custom_domain

    Site.objects.update_or_create(defaults=site_params, id=1)


class Migration(migrations.Migration):
    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(create_site),
    ]
