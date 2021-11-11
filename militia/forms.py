from django import forms
from militia.models import Tip

class TipForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label="Title")
    message = forms.Textarea()
    location = forms.Textarea()
    pin_code = forms.CharField(label="Pin Code", max_length=100, required=False)
    date = forms.DateTimeField(label="Date", widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Tip
        fields = ("title", "message", "location", "pin_code", "date", "file")

    def __str__(self):
        return self.title