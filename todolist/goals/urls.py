from django.urls import path, include

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

    path('board/', include((
        [
            path('create', boards.BoardCreateView.as_view(), name='create'),
            path('<pk>', boards.BoardView.as_view(), name='main'),
            path('list', boards.BoardListView.as_view(), name='list'),
        ], 'board'), namespace='board'))
]
