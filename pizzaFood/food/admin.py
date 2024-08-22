from django.contrib import admin
from .models import Pizza, Order, OrderItem

# Configuration de l'affichage du modèle Pizza dans l'admin
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')  # Colonnes à afficher dans la liste
    search_fields = ('name', 'description')  # Champs pour la recherche
    list_filter = ('price',)  # Filtres disponibles dans la barre latérale

# Configuration de l'affichage du modèle OrderItem dans l'admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Nombre de formulaires vierges à afficher

# Configuration de l'affichage du modèle Order dans l'admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone', 'ordered_at', 'total_price')
    search_fields = ('customer_name', 'customer_phone')
    list_filter = ('ordered_at',)
    inlines = [OrderItemInline]  # Afficher les OrderItems associés directement dans le formulaire d'édition d'une commande

# Enregistrement des modèles dans l'administration
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)
