from django import forms

from .models import UserName


class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Введите ваше имя", "autofocus": True}),
        }
        error_messages = {
            "name": {
                "required": "Пожалуйста, введите имя.",
                "max_length": "Имя слишком длинное (максимум 100 символов).",
            }
        }
