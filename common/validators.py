import os
from rest_framework import serializers
from django.core.exceptions import ValidationError
from common.constants import DOCUMENT_TEMPLATE_FILE_ALLOWED_EXTENSIONS, DOCUMENT_TEMPLATE_MAX_FILE_SIZE, \
    IMAGE_MAX_FILE_SIZE, IMAGE_ALLOWED_EXTENSIONS
MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.jpg','.jpeg', '.png']


def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'max file size is: {MAX_FILE_SIZE}')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')

def num_pages_range_validation(value):
    if not (1 <= value <= 1000):
        raise serializers.ValidationError('Invalid num pages value')


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() in DOCUMENT_TEMPLATE_FILE_ALLOWED_EXTENSIONS:
        raise ValidationError('Unsupported file extension.')


def validate_file_size(value):
    if value.size > DOCUMENT_TEMPLATE_MAX_FILE_SIZE:  # 10 MB
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    else:
        return value


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() in IMAGE_ALLOWED_EXTENSIONS:
        raise ValidationError('Unsupported file extension.')


def validate_image_size(value):
    if value.size > IMAGE_MAX_FILE_SIZE:  # 10 MB
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    else:
        return value
