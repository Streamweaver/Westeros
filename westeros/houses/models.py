from django.db import models

class HouseAttributes(models.Model):
    """
    Base abstract house model for the all house attributes.
    """
    defense_help = "Defensive strength of House land and holdings."
    defense = models.IntegerField(default=0, help_text=defense_help)

    influence_help = "Measure of political power."
    influence = models.IntegerField(default=0, help_text=influence_help)

    lands_help = "Size of Hosuehold lands."
    lands = models.IntegerField(default=0, help_text=lands_help)

    law_help = "The level or law and order in the territory."
    law = models.IntegerField(default=0, help_text=law_help)

    population_help = "Density and size of population on Household lands."
    population = models.IntegerField(default=0, help_text=population_help)

    power_help = "Military Strength of the Household."
    power = models.IntegerField(default=0, help_text=power_help)

    wealth_help = "Overall wealth of the Household."
    wealth = models.IntegerField(default=0, help_text=wealth_help)

    # Tracking Information
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Realm(HouseAttributes):
    """
    The major region for the household.
    """
    name_help = "Name of the realm the house belongs to in Westeros."
    name = models.CharField(max_length=100, help_text=name_help)

    def __unicode__(self):
        return u'%s' % self.name

    def __str_(self):
        return '%s' % self.__unicode__(self)

    def save(self, *args, **kwargs):
        """Triggers a recalculation of House values on save."""
        super(Realm, self).save(*args, **kwargs)
        # Adjust all related houses as needed.
        # This calls calculate and save indescriminantly but this shouldn't be
        # a problem as realms aren't often updated or created.
        for house in self.house_set.all():
            house.calculate()
            house.save()

    class Meta:
        ordering = ['name']

class House(HouseAttributes):
    """
    Noble House of Westeros.
    """
    name_help = "House Name."
    name = models.CharField(max_length=100, help_text=name_help)

    desc_help = "Information about the Household."
    description = models.TextField(null=True, blank=True, help_text=desc_help)

    realm_help = "Realm in Westeros the House belongs to."
    realm = models.ForeignKey(Realm)

    def __init__(self, *args, **kwargs):
        super(House, self).__init__(*args, **kwargs)
        self.old_realm = self.realm

    def calculate(self):
        """
        Derives house attributes by summing all relavant subattributes.
        """
        attributes = {
            "defense": 0,
            "influence": 0,
            "lands": 0,
            "law": 0,
            "population": 0,
            "power": 0,
            "wealth": 0,
        }

        for attr in attributes:
            attributes[attr] += getattr(self.baseattributes, attr)
            attributes[attr] += getattr(self.realm, attr)
            attributes[attr] += getattr(self.destinycharacters, attr)
            for event in self.event_set.all():
                attributes[attr] += getattr(event, attr)
            setattr(self, attr, attributes[attr])

    def __unicode__(self):
        return u'House %s of %s' % (self.name, self.realm)

    def __str__(self):
        return "%s" % self.__unicode__()

    def save(self, *args, **kwargs):
        if self.realm is not self.old_realm:
            self.calculate()
        super(House, self).save(*args, **kwargs)

    class Meta:
        unique_together = (("realm", "name"))
        ordering = ['name', 'realm']


class Founding(models.Model):
    """
    The time period of the founding of the household.
    """
    PERIODS = (
        ('dr', "Days of Dragons"),
        ('wu', "War of the Usurper")
    )

    house = models.OneToOneField(House, primary_key=True)

    period_help = "Name of the age the house was founded in."
    period = models.CharField(max_length=2, choices=PERIODS, help_text=period_help)

    events_help = "Number of significan events in the houses founding."
    events = models.IntegerField(default=0, help_text=events_help)

class BaseAttributes(HouseAttributes):
    """
    The base attributes determined for the Household without any other
    modifications.
    """
    house = models.OneToOneField(House, primary_key=True)

    def save(self, *args, **kwargs):
        """Triggers a recalculation of House values on save."""
        super(BaseAttributes, self).save(*args, **kwargs)
        self.house.calculate()
        self.house.save()

class DestinyCharacters(HouseAttributes):
    """
    The number of inviduals in a Household considered 'Destiny Characters'.
    This normally applies to the number of players in a household but could
    otherwise represent the equivalent value characters with a destiny.
    """
    house = models.OneToOneField(House, primary_key=True)

    char_help = "The number of Destiny Characters in the Household."
    number = models.PositiveIntegerField(help_text=char_help)

    def save(self, *args, **kwargs):
        """Triggers a recalculation of House values on save."""
        super(DestinyCharacters, self).save(*args, **kwargs)
        self.house.calculate()
        self.house.save()

class Event(HouseAttributes):
    """
    Events that effect or modify house attributes.
    """
    TYPES = (
        ("gl", "Glory"),
        ("sc", "Scandle")
    )

    name_help = "Name the folk know the event by."
    name = models.CharField(max_length=255, null=True, blank=True, help_text=name_help)

    type_help = "Type of Event."
    type = models.CharField(max_length=2,choices=TYPES, help_text=type_help)

    house_help = "House the Event Effected."
    house = models.ForeignKey(House, help_text=house_help)

    years_help = "Number of years ago the event Happened."
    years = models.PositiveIntegerField(null=True, blank=True, help_text=years_help)

    desc_help = "Description of the Event."
    description = models.TextField(null=True, blank=True, help_text=desc_help)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.house)

    def save(self, *args, **kwargs):
        """Triggers a recalculation of House values on save."""
        if self.name:
            self.name = TYPES[self.type]
        super(Event, self).save(*args, **kwargs)
        self.house.calculate()
        self.house.save()