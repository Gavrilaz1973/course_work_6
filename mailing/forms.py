from django import forms

from mailing.models import Message, Client


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'  #exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'  #exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'