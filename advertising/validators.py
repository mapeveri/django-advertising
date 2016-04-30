from django.core.exceptions import ValidationError


def valid_extension(value):
    """
    Function that valid extension
    when upload file in form
    """
    if (not value.name.endswith('.png') and
        not value.name.endswith('.jpeg') and
        not value.name.endswith('.gif') and
        not value.name.endswith('.bmp') and
        not value.name.endswith('.jpg')):

        text = "Files allowed"
        files = ".jpg, .jpeg, .png, .gif, .bmp"
        raise ValidationError(text + ': ' + files)