from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

def validate_custom_username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError("This username is already taken.")
    if not username.isalnum():
        raise ValidationError("Username must contain only letters and numbers.")
    min_length = 3
    max_length = 30
    if len(username) < min_length or len(username) > max_length:
        raise ValidationError(f"Username must be between {min_length} and {max_length} characters long.")



def validate_custom_password(password):
    try:
        validate_password(password)
    except ValidationError as e:
        raise ValidationError("\n".join(e.messages))
