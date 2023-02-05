from django.urls import path

from . import views

app_name = "polls"

# /polls/xxx というリクエストに対して、DjangoはROOT_URLCONFに指定されているpythonモジュールをロードする。(この場合はurls.py)
# そのモジュール内のurlpatternsという変数を探し、順番に検査していく。
# /polls/5/ とリクエストすると、`detail(request=<HttpRequest object>, question_id=5)` という呼び出しを行う。
urlpatterns = [
    # http://localhost:8000/polls/ のアクセス先
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote", views.vote, name="vote"),
]
