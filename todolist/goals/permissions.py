from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from goals.models import BoardParticipant


class BoardPermissions(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if not request.user.is_authenticated:
            return False

        filters: dict = {'user': request.user, 'board': obj}
        if request.method not in permissions.SAFE_METHODS:
            filters['role'] = BoardParticipant.Role.OWNER

        return BoardParticipant.objects.filter(**filters).exists()


class GoalCategoryPermissions(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if not request.user.is_authenticated:
            return False

        filters: dict = {'user': request.user, 'board': obj.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.OWNER, BoardParticipant.Role.WRITER]

        return BoardParticipant.objects.filter(**filters).exists()


class GoalPermissions(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if not request.user.is_authenticated:
            return False

        filters: dict = {'user': request.user, 'board': obj.category.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.OWNER, BoardParticipant.Role.WRITER]

        return BoardParticipant.objects.filter(**filters).exists()


class CommentsPermissions(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if not request.user.is_authenticated:
            return False

        if request.method not in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
