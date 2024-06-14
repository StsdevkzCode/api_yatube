from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для постов.
    Добавляет поле author, доступное только для чтения.
    """
    author = serializers.ReadOnlyField(
        source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для комментариев.
    Добавляет поля author и post, доступные только для чтения.
    """
    author = serializers.ReadOnlyField(
        source='author.username', read_only=True)
    post = serializers.ReadOnlyField(source='post.id', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
