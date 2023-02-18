from django import forms
from .models import Kwitantie
from .input_fields import hour_list, tarief_dict


class KwitantieAanmaken(forms.Form):
    project = forms.CharField()
    tarief = forms.ChoiceField(choices=[(v, k) for k, v in tarief_dict().items()])
    beschrijving = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Eventuele details (max 700 tekens).'}),
                                   label='Aanvullende informatie',
                                   required=True,
                                   max_length=700)
    aantal_uren = forms.ChoiceField(label='aantal minuten',
                                    choices=hour_list()
                                    )
    naam = forms.CharField(label='Naam of bedrijfsnaam',
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Example BV'}))
    straat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'voorbeeldweg'}))
    nummer = forms.CharField(label='Huisnummer', widget=forms.TextInput(attrs={'placeholder': '15'}))
    postcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '1234 AB'}))
    plaats = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Den Haag'}))
    land = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nederland'}))

    def clean(self):
        super(KwitantieAanmaken, self).clean()
        self.kwitantie = Kwitantie(aantal_uren=self.cleaned_data['aantal_uren'],
                                   beschrijving=self.cleaned_data['beschrijving'],
                                   project=self.cleaned_data['project'],
                                   naam=self.cleaned_data['naam'],
                                   straat=self.cleaned_data['straat'],
                                   nummer=self.cleaned_data['nummer'],
                                   postcode=self.cleaned_data['postcode'],
                                   plaats=self.cleaned_data['plaats'],
                                   land=self.cleaned_data['land']
                                   )