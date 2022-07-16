from django import forms


class RoomEditForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    city = forms.CharField()
    price = forms.IntegerField()
    address = forms.CharField()
    guests = forms.IntegerField()
    beds = forms.IntegerField()
    bedrooms = forms.IntegerField()
    baths = forms.IntegerField()
    check_in = forms.CharField()
    check_out = forms.CharField()
    instant_book = forms.BooleanField()
    room_type = forms.CharField()
    amenities = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "basic_input"})
    )
    facilities = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "basic_input"})
    )
    house_rules = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "basic_input"})
    )

    def __init__(self, *args, **kwargs):
        room = kwargs.pop("room", None)
        super(RoomEditForm, self).__init__(*args, **kwargs)
        self.fields["name"].initial = room.name
        self.fields["description"].initial = room.description
        self.fields["city"].initial = room.city
        self.fields["price"].initial = room.price
        self.fields["address"].initial = room.address
        self.fields["guests"].initial = room.guests
        self.fields["beds"].initial = room.beds
        self.fields["bedrooms"].initial = room.bedrooms
        self.fields["baths"].initial = room.baths
        self.fields["check_in"].initial = room.check_in
        self.fields["check_out"].initial = room.check_out
        self.fields["instant_book"].initial = room.instant_book
        self.fields["room_type"].initial = room.room_type
