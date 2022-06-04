from django.contrib import admin

from goals.models import GoalCategory, GoalComment, Goal, Board, BoardParticipant


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")
    list_filter = ("is_deleted",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "due_date")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")
    list_filter = ("status", "priority")


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("goal_id", "text")
    list_display_links = ("text",)
    search_fields = ("text",)
    readonly_fields = ("created", "updated")


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated")
    search_fields = ("title",)
    list_filter = ("is_deleted",)
    readonly_fields = ("created", "updated")


@admin.register(BoardParticipant)
class BoardParticipantAdmin(admin.ModelAdmin):
    list_display = ("user", "board", "role", "created", "updated")
    search_fields = ("user__username", "board__title")
    readonly_fields = ("created", "updated")
