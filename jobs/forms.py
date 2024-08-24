from django import forms


class JobSearchForm(forms.Form):
    job_title = forms.CharField(label='Job Title', max_length=255, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Search By Job Title'}))
