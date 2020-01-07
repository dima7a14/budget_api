from django.contrib import admin

from .models import Family
from .forms import FamilyCreationForm, FamilyChangeForm


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    """Defines admin model for family model."""
    add_form = FamilyCreationForm
    form = FamilyChangeForm
    model = Family
    list_display = ['name', 'created_at', 'updated_at', 'owner']
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Users', {'fields': ('owner', 'members')}),
    )
    search_fields = ('name', 'owner', 'members')
    ordering = ('created_at', 'updated_at')
