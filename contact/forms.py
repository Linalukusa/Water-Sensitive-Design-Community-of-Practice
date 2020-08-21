# make sure this is at the top if it isn't already
from django import forms

# our new form
class Contact (forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

 # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name:"
        self.fields['email'].label = "Your email:"
        self.fields['content'].label =
            "What do you want to say?"