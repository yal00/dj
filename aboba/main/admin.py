from django.contrib import admin
from .models import Homeblocks, Demand, Geo, Topskills, Chart, Chart2, Chart3

admin.site.register(Homeblocks)

class ChartInline(admin.StackedInline):
    model = Chart
    extra = 1

class ChartGeoInline(admin.StackedInline):
    model = Chart2
    extra = 1

class ChartTopskillsInline(admin.StackedInline):
    model = Chart3
    extra = 1

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    inlines = [ChartInline]

@admin.register(Geo)
class GeoAdmin(admin.ModelAdmin):
    inlines = [ChartGeoInline]

@admin.register(Topskills)
class TopskillsAdmin(admin.ModelAdmin):
    inlines = [ChartTopskillsInline]


