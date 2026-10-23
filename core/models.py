from django.db import models

class SiteSettings(models.Model):
    POSITION_CHOICES = [
        ('left center', 'Gauche'),
        ('center center', 'Centre'),
        ('right center', 'Droite'),
    ]

    # --- Hero ---
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    hero_image_position = models.CharField(max_length=30, choices=POSITION_CHOICES, default='right center')

    hero_eyebrow_fr = models.CharField(max_length=100, default="LIND'S PREMIUM AFFAIRS")
    hero_eyebrow_en = models.CharField(max_length=100, default="LIND'S PREMIUM AFFAIRS")

    hero_title_fr = models.CharField(max_length=200, default="UN MONDE D'<em>AFFAIRES RAFFINÉES.</em>")
    hero_title_en = models.CharField(max_length=200, default="A WORLD OF <em>REFINED AFFAIRS.</em>")

    hero_subtitle_fr = models.TextField(default="We Elevate Experiences. Des collections soignées...")
    hero_subtitle_en = models.TextField(default="We Elevate Experiences. Thoughtful collections...")

    hero_cta_fr = models.CharField(max_length=50, default="DÉCOUVRIR LPA")
    hero_cta_en = models.CharField(max_length=50, default="DISCOVER LPA")
    hero_cta_url = models.CharField(max_length=200, default="#about")

    # --- Contact & WhatsApp ---
    whatsapp_number = models.CharField(max_length=30, blank=True, help_text="Ex: 237600000000 (sans le +)")
    whatsapp_message_fr = models.TextField(blank=True, default="Bonjour LPA, je souhaite avoir plus d'informations.")
    whatsapp_message_en = models.TextField(blank=True, default="Hello LPA, I would like to have more information.")
    contact_email = models.EmailField(blank=True, help_text="Adresse Gmail professionnelle")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paramètres du site"
        verbose_name_plural = "Paramètres du site"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Paramètres LPA"


class AboutBlock(models.Model):
    """Les blocs de la section À propos (Mission, Vision, etc.)"""
    title_fr = models.CharField(max_length=100, verbose_name="Titre (Français)")
    title_en = models.CharField(max_length=100, verbose_name="Titre (Anglais)")
    content_fr = models.TextField(verbose_name="Contenu (Français)")
    content_en = models.TextField(verbose_name="Contenu (Anglais)")
    order_index = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['order_index']
        verbose_name = "Bloc À propos"
        verbose_name_plural = "Blocs À propos"

    def __str__(self):
        return self.title_fr


class Service(models.Model):
    slug = models.SlugField(unique=True, help_text="Identifiant unique (ex: accessories)")
    name_fr = models.CharField(max_length=100, verbose_name="Nom (Français)")
    name_en = models.CharField(max_length=100, verbose_name="Nom (Anglais)")
    description_fr = models.TextField(verbose_name="Description (Français)", blank=True)
    description_en = models.TextField(verbose_name="Description (Anglais)", blank=True)
    price_fr = models.CharField(max_length=100, blank=True, verbose_name="Prix (Français)")
    price_en = models.CharField(max_length=100, blank=True, verbose_name="Prix (Anglais)")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Image du service")
    order_index = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    is_active = models.BooleanField(default=True, verbose_name="Affiché sur le site")

    class Meta:
        ordering = ['order_index']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name_fr


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE, verbose_name="Service associé")
    image = models.ImageField(upload_to='services/gallery/', verbose_name="Photo")
    title_fr = models.CharField(max_length=100, blank=True, verbose_name="Titre (Français)", help_text="Optionnel")
    title_en = models.CharField(max_length=100, blank=True, verbose_name="Titre (Anglais)", help_text="Optionnel")
    order_index = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['order_index']
        verbose_name = "Photo de la galerie"
        verbose_name_plural = "Galerie photos"

    def __str__(self):
        return f"Photo pour {self.service.name_fr} - {self.title_fr or 'Sans titre'}"