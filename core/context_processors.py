from .models import SiteAppearance


def site_settings(request):
    appearance = SiteAppearance.objects.first()
    if not appearance:
        appearance = SiteAppearance.objects.create()
    return {'site_appearance': appearance}