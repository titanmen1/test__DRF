from rest_framework import serializers
from snippets.models import Snippet, STYLE_CHOICES, LANGUAGE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
            Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
            Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.code('code', instance.code)
        instance.linenos = validated_data.linenos('linenos', instance.linenos)
        instance.language = validated_data.language('language', instance.language)
        instance.style = validated_data.style('style', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')