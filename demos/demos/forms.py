from django import forms


class UserForm(forms.Form):
    textone = forms.CharField(
        label='ファイル',
        widget=forms.TextInput(
            attrs={
                'id': 'dropedfile'}))

    areaone = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'id': 'resultbase64',
                "rows": 20,
                "cols": 10,
            }
        )
    )
