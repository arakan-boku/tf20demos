from django.shortcuts import render
from . import forms
from django.template.context_processors import csrf
from .tf20 import vgg16_imagenet as cl
from . import typo_v2 as t2
from . import textsum as apido
from . import talk


# 応答用の辞書を組み立てて返す
def __makedic(k, txt):
    return {'k': k, 'txt': txt}


def talk_do(request):
    t = talk.Talk()
    if request.method == 'POST':
        # テキストボックスに入力されたメッセージ
        q = request.POST["texttwo"]
        # Talk-APIからの応答メッセージ取得
        a = t.get(q)
        # 描画用リストに最新のメッセージを格納する
        talktxts = []
        talktxts.append(__makedic('ai', a))
        talktxts.append(__makedic('b', q))
        # 過去の応答履歴をセッションから取り出してリストに追記する
        saveh = []
        if 'hist' in request.session:
            hists = request.session['hist']
            saveh = hists
            for h in reversed(hists):
                x = h.split(':')
                talktxts.append(__makedic(x[0], x[1]))
        # 最新のメッセージを履歴に加えてセッションに保存する
        saveh.append('b:' + q)
        saveh.append('ai:' + a)
        request.session['hist'] = saveh
        # 描画準備
        form = forms.UserForm(label_suffix='：')
        c = {
            'form': form,
            'texttwo': '',
            'talktxts': talktxts
        }
    else:
        # 初期表示の時にセッションもクリアする
        request.session.clear()
        # フォームの初期化
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'talk.html', c)


def summarize(request):
    api = apido.TextSummarize()
    if request.method == 'POST':
        # テキストボックスに入力されたメッセージ
        input_text = request.POST["areathree"]
        # APIリクエストを投げてからの応答を取得
        rets = api.get(input_text)
        c = {
            'areathree': input_text,
            'results': rets
        }
        return render(request, 'textsum_result.html', c)
    else:
        # 初期表示の時にセッションもクリアする
        request.session.clear()
        # フォームの初期化
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
        return render(request, 'textsum.html', c)


def proofread(request):
    api = t2.TypoV2()
    if request.method == 'POST':
        # テキストボックスに入力されたメッセージ
        input_text = request.POST['areatwo']
        # APIリクエストを投げてからの応答を取得
        rets = api.get(input_text)
        form = forms.UserForm(initial={'areatwo': input_text})
        c = {
            'form': form,
            'areatwo': input_text,
            'rets': rets
        }
    else:
        # 初期表示の時にセッションもクリアする
        request.session.clear()
        # フォームの初期化
        form = forms.UserForm(label_suffix='：')
        rets = '''入力されたテキストで文法的に疑わしい部分を指摘します。</br>
                疑わしい部分とは以下のような部分です。</br>
                ・誤字の可能性が高い部分。</br>
                ・誤字では無いが珍しい使い方。</br>
                ・他により良い表現がありそうな部分。'''
        c = {'form': form,
             'rets': rets
             }
    c.update(csrf(request))
    return render(request, 'typo.html', c)


def dropdemo(request):
    if request.method == 'POST':
        img = request.POST["areaone"]
        if('data:image/jpeg' in img):
            decode_img = img.replace('data:image/jpeg;base64,', '')
        else:
            decode_img = img.replace('data:image/png;base64,', '')
        model = cl.Vgg16k()
        ans = model.predict_from_base64(decode_img)
        c = {
            'base64text': img,
            'decodeimg': decode_img,
            'enlabel': ans['en'],
            'jplabel': ans['jp'],
            'pplabel': ans['pp'],
        }
    else:
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'dragdrop.html', c)


def freedraw(request):
    if request.method == 'POST':
        c = {
            'base64text': request.POST["areaone"],
        }
    else:
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'canvas01.html', c)
