from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     # テンプレートをロードしてコンテキストに値を入れ、テンプレートをレンダリングした結果を HttpResponse オブジェクトで返す。というショートカット。
#     return render(request, "polls/index.html", context)

# 汎用ビュー。
# よくあるパターンを抽象化して、Python コードすら書かずにアプリケーションを書き上げられる状態にしたもの
# つまりデフォルトで、いろんな操作をして諸々の変数を生成してくれて、それらを元に各テンプレートを呼び出すことができる。
class IndexView(generic.ListView):  #  ListViewは、オブジェクトのリストを表示する汎用ビュー
    template_name = "polls/index.html"  # デフォルトでは、<app name>/<model name>_list.html というテンプレートを使う。

    # ListView では、自動的に生成されるコンテキスト変数は question_list になる。
    # これを上書きするには、context_object_name 属性を与え、文字列で変数名を指定する。
    # ここで言うcontextとは、辞書型のデータで、as_view()を実行後に実行されるget_context_data()で取得されるデータ。
    # contextには、pagination関連やQueryset関連、View関連(template_nameから引っ張ってきたhtmlも含む)の情報が入っている。
    # コンテキスト変数(置換変数)とは、IndexViewクラスのインスタンスが開始されるまで解決されることのない変数を参照できる。インスタンス生成時に置換される。インスタンス内でグローバルな変数。
    context_object_name = "latest_question_list"

    # これは多分、get_context_data() でデフォルトではQuestionのデータをすべて返すので、
    # 代わりにこのクエリを使うよう指定しているはず。
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except:
#         # class django.http.Http404
#         # ビュー関数のどの場所でも、django が認識して標準的なエラーページをアプリケーションに返してくれる。
#         # 独自の HTML を表示したいときは、`404.html` という名前の HTML テンプレートを作成し、テンプレートツリーのトップレベルの場所に置いて、DEBUG を False にする。
#         raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# DetailView 汎用ビューには、"pk"という名前で URL からプライマリキーをキャプチャして渡すことになっているため、URLパラメータ内にデータ検索用の pk が必要。
# そのpkを元に get して、コンテキスト変数 question が自動生成される。多分モデル名の全小文字になる。
class DetailView(generic.DetailView):  #  DetailViewは、あるタイプのオブジェクトの詳細ページを表示する汎用ビュー
    model = Question  # 各汎用ビューは自分がどのモデルに対して動作するのか知っておく
    template_name = "polls/detail.html"  # デフォルトは、<app name>/<model name>_detail.html というテンプレートを使う。

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST は、辞書のようなオブジェクト。postメソッドでの呼び出しにおいてのみ参照可能。request.GET もある。
        # POSTデータに choice キーがなければ、KeyErrorになる。
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, "polls/detail.html", {"question": question, "error_message": "You didn't select a choice"}
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST データを正常に処理した後は、常に HttpResponseRedirect を返す。これはWebで一般的なやり方。
        # Redirectのコンストラクタには、リダイレクト先のURLを渡す。
        # reverse()関数は、制御を渡したいビューの名前と、そのビューに与えるURLパターンの位置引数を与えると、文字列でURLを返す。
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
