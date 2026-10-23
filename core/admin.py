from django.contrib import admin
from .models import SiteSettings, Service, ServiceImage, AboutBlock

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Hero — Image", {'fields': ('hero_image', 'hero_image_position')}),
        ("Hero — Textes FR", {'fields': ('hero_eyebrow_fr', 'hero_title_fr', 'hero_subtitle_fr', 'hero_cta_fr')}),
        ("Hero — Textes EN", {'fields': ('hero_eyebrow_en', 'hero_title_en', 'hero_subtitle_en', 'hero_cta_en')}),
        ("Bouton & Contact", {'fields': ('hero_cta_url',)}),
        ("WhatsApp", {'fields': ('whatsapp_number', 'whatsapp_message_fr', 'whatsapp_message_en')}),
        ("Email", {'fields': ('contact_email',)}),
    )
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    list_display = ('title_fr', 'title_en', 'order_index')
    list_editable = ('order_index',)

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'name_en', 'order_index', 'is_active')
    list_editable = ('order_index', 'is_active')
    prepopulated_fields = {'slug': ('name_fr',)}
    fieldsets = (
        ("Informations de base", {'fields': ('slug', 'image', 'order_index', 'is_active')}),
        ("Version Française", {'fields': ('name_fr', 'description_fr', 'price_fr')}),
        ("Version Anglaise", {'fields': ('name_en', 'description_en', 'price_en')}),
    )
    inlines = [ServiceImageInline]