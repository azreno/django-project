from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="А теперь возраст", initial=18, min_value=1, max_value=150)
    comm = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea,
        initial="комментируйте, а мы это никуда не отошлём",
        help_text="чего ждёшь?",
        required=False,
        min_length=2,
        max_length=50,
    )
