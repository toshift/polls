from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Posting
from .forms import PostingForm
from django.contrib import messages

def _get_page(list_, page_no, count=5):
    """ページネーターを使い、表示するページ情報を取得する"""
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        # page_noが指定されていない場合、数値でない場合、範囲外の場合は先頭ページを表示する
        page = paginator.page(1)
    return page


def index(request):
    """表示、投稿を処理する"""
    # ModelFormもFormもインスタンスを作るタイミングでの使い方は同じ
    form = PostingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # save()メソッドを呼ぶだけでModelを使ってDBに登録される
            form.save()
            messages.success(request, '投稿されました')
            return redirect('guestboard:index')
        else:
            messages.error(request, '入力に誤りがあります')
    page = _get_page( Posting.objects.order_by('-id'), # 投稿を新しい順に並び替え
                     request.GET.get('page')) # GETクエリからページ番号を取得する ?
    contexts = {
        'form': form,
        'page': page,
    }
    return render(request, 'guestboard/index.html', contexts) 
                     
