from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.core.files.storage import default_storage
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
            "birth_date",
        )

# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User

class SigleUploadForm(forms.Form):
    file = forms.ImageField(label="image file")

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)
    