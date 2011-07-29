#
# Copyright 2011 Scott Turnbull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib import admin

from westeros.houses.models import House, Realm, Event, BaseAttributes, Founding, DestinyCharacters

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