from django import forms


class UserForm(forms.Form):
    textone = forms.CharField(
        label='ファイル',
        widget=forms.TextInput(
            attrs={
                'id': 'dropedfile'}))

    texttwo = forms.CharField(
        label='話す',
        widget=forms.TextInput(
            attrs={
                'id': 'dropedfile',
                'placeholder': 'ここに会話文を入力します。',
            }))

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

    areatwo = forms.CharField(
        label='元文章',
        max_length=500,
        min_length=1,
        widget=forms.Textarea(
            attrs={
                'id': 'typov2',
                'placeholder': 'ここにチェックしたい文章を入力してください(500文字迄）。',
                'rows': 10,
                'cols': 5,
            }))

    areathree = forms.CharField(
        label='要約元文章',
        max_length=200,
        min_length=20,
        widget=forms.Textarea(
            attrs={
                'id': 'commu',
                'placeholder': 'ここに要約したい文章を入力してください(200文字迄）。',
                'rows': 10,
                'cols': 5,
            }))
