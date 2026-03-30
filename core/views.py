from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from .forms import AppearanceForm
from .models import TeamMember, SiteAppearance
from .utils import user_can_edit


def home(request):
    members = TeamMember.objects.all()
    can_edit = user_can_edit(request.user)
    return render(request, 'home.html', {
        'members': members,
        'can_edit': can_edit,
    })


@login_required
def edit_appearance(request):
    if not user_can_edit(request.user):
        raise PermissionDenied("Kamu tidak punya izin untuk mengubah tampilan.")

    appearance = SiteAppearance.objects.first()
    if not appearance:
        appearance = SiteAppearance.objects.create()

    if request.method == 'POST':
        form = AppearanceForm(request.POST, instance=appearance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppearanceForm(instance=appearance)

    return render(request, 'edit_appearance.html', {'form': form})