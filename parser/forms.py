from django import forms 

from . import parse_cars , models

class CarParseForm(forms.Form):
    MEDIA_CHOICES = {
        ('CARS_KG','CARS_KG'),
    }
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['send'] == 'Delete':
            models.Car.objects.all().delete()
            return 0
        if self.data['media_type'] == 'CARS_KG':
            car_parser = parse_cars.parser()
            if len(car_parser) > 0:
                for i in car_parser:
                    models.Car.objects.create(**i)
                return 1 
        return 0