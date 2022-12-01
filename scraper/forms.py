from django import forms


class Cakes(forms.Form):

    first_cake = forms.CharField(max_length=100, required=False)
    second_cake = forms.CharField(max_length=100, required=False)
    third_cake = forms.CharField(max_length=100, required=False)
    fourth_cake = forms.CharField(max_length=100, required=False)