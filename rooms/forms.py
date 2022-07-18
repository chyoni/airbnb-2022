from django import forms

from rooms import models


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
    instant_book = forms.BooleanField(required=False)
    room_type = forms.CharField()
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "basic_input"}),
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "basic_input"}),
    )
    house_rules = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.HouseRule.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "basic_input"}),
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
        self.fields["room_type"].initial = room.room_type.pk

    def save(self, room):

        new_name = self.cleaned_data["name"]
        new_description = self.cleaned_data["description"]
        new_city = self.cleaned_data["city"]
        new_price = self.cleaned_data["price"]
        new_address = self.cleaned_data["address"]
        new_guests = self.cleaned_data["guests"]
        new_beds = self.cleaned_data["beds"]
        new_bedrooms = self.cleaned_data["bedrooms"]
        new_baths = self.cleaned_data["baths"]
        new_check_in = self.cleaned_data["check_in"]
        new_check_out = self.cleaned_data["check_out"]
        new_instant_book = self.cleaned_data["instant_book"]
        new_room_type = self.cleaned_data["room_type"]
        new_amenities = self.cleaned_data["amenities"]
        new_facilities = self.cleaned_data["facilities"]
        new_house_rules = self.cleaned_data["house_rules"]

        models.Room.objects.filter(pk=room.pk).update(
            name=new_name,
            description=new_description,
            city=new_city,
            price=new_price,
            address=new_address,
            guests=new_guests,
            beds=new_beds,
            bedrooms=new_bedrooms,
            baths=new_baths,
            check_in=new_check_in,
            check_out=new_check_out,
            instant_book=new_instant_book,
            room_type=new_room_type,
        )

        if len(new_amenities) > 0:
            room.amenities.clear()
            for a in new_amenities:
                room.amenities.add(a)

        if len(new_facilities) > 0:
            room.facilities.clear()
            for f in new_facilities:
                room.facilities.add(f)

        if len(new_house_rules) > 0:
            room.house_rules.clear()
            for r in new_house_rules:
                room.house_rules.add(r)


class EditPhotoForm(forms.Form):

    caption = forms.CharField(required=True, max_length=180)

    def __init__(self, *args, **kwargs):
        photo = kwargs.pop("photo", None)
        super(EditPhotoForm, self).__init__(*args, **kwargs)
        self.fields["caption"].initial = photo.caption

    def save(self, photo_pk):

        photo = models.Photo.objects.get(pk=photo_pk)
        photo.caption = self.cleaned_data["caption"]
        photo.save()


class UploadPhotoForm(forms.Form):

    upload_photo = forms.ImageField()
    caption = forms.CharField(required=True, max_length=180)

    def save(self, room):

        room = models.Room.objects.get(pk=room.pk)
        photo = self.cleaned_data["upload_photo"]

        new_photo = models.Photo.objects.create(
            caption=self.cleaned_data["caption"],
            file=photo,
            room=room,
        )
        new_photo.save()
