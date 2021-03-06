from django import forms
from wealthmap import models as wm_models


class SearchModelForm(forms.ModelForm):

    class Meta:
        model = wm_models.get_search_model()
        exclude = []
        widgets = {
            "creator": forms.HiddenInput(),
        }
