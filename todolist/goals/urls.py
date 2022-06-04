from django.urls import path

from goals.views import category, goals, comments, boards

urlpatterns = [
    path("goal_category/create", category.GoalCategoryCreateView.as_view()),
    path("goal_category/list", category.GoalCategoryListView.as_view()),
    path("goal_category/<pk>", category.GoalCategoryView.as_view()),

    path("goal/create", goals.GoalCreateView.as_view()),
    path("goal/list", goals.GoalListView.as_view()),
    path("goal/<pk>", goals.GoalView.as_view()),

    path("goal_comment/create", comments.CommentCreateView.as_view()),
    path("goal_comment/list", comments.CommentListView.as_view()),
    path("goal_comment/<pk>", comments.CommentView.as_view()),

    path("board/create", boards.BoardCreateView.as_view()),
    path("board/<pk>", boards.BoardView.as_view()),
    path("board/list", boards.BoardListView.as_view()),
   ]
