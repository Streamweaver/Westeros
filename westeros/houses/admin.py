from django.contrib import admin

from asoiaf.houses.models import House, Realm, Event, BaseAttributes, Founding, DestinyCharacters

class RealmAdmin(admin.ModelAdmin):
    fields = ["name", "defense", "influence", "lands", "law", "population",
                "power", "wealth",]

admin.site.register(Realm, RealmAdmin)

class BaseAttributesInline(admin.TabularInline):
    model = BaseAttributes

class FoundingInline(admin.StackedInline):
    model = Founding

class DestinyInline(admin.TabularInline):
    model = DestinyCharacters
    fields = ["number", "defense", "influence", "lands", "law", "population",
                "power", "wealth",]

class EventsInline(admin.TabularInline):
    model = Event
    fields = ["name", "type", "defense", "influence", "lands", "law", "population",
                "power", "wealth",]

class HouseAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ("name", "realm", "description")
            }),
        ("Attributes", {
            'classes': ('collapse',),
            'fields': ("defense", "influence", "lands", "law", "population", "power", "wealth"),
            })
    )
    inlines = [BaseAttributesInline, DestinyInline, FoundingInline, EventsInline]
    
admin.site.register(House, HouseAdmin)