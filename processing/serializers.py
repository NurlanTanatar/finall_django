from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from processing.models import Book, Journal
from common.validators import num_pages_range_validation


class BookSerializer(serializers.ModelSerializer):
    num_pages = serializers.IntegerField(validators=[num_pages_range_validation])

    class Meta:
        model = Book
        fields = '__all__'

    # def validate_num_pages(self, value):
    #     if value > 1000:
    #         raise ValidationError('must be less than or equal to 1000')
    #     return value
    #
    # def validate(self, attrs):
    #     if attrs['num_pages'] > 1000:
    #         raise ValidationError({'num_pages': 'must be less than or equal to 1000'})
    #     return attrs


class BookDetailSerializer(BookSerializer):
    cover = serializers.ImageField(write_only=True, required=False)
    document = serializers.FileField(write_only=True, required=False)
    cover_url = serializers.SerializerMethodField(read_only=True)
    document_url = serializers.SerializerMethodField(read_only=True)

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ('book_authors', 'cover_url', 'document_url', 'cover', 'document')

    def get_cover_url(self, obj):
        if obj.cover:
            return self.context['request'].build_absolute_uri(obj.cover.url)
        return None

    def get_document_url(self, obj):
        if obj.document:
            return self.context['request'].build_absolute_uri(obj.document.url)
        return None
