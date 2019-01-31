#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import numpy as np

#
def index(request):
    return HttpResponse('Hello World ,from test1')
#
def predict_input(request):
    from test1.include.pred_price import  PredPrice
    return render(request, 'test1/predict_input.html')
#
def predict(request):
    if request.method == 'POST':
        from test1.include.pred_price import  PredPrice
        siki_price=request.POST['siki_price']
        rei_price =request.POST['rei_price']
        menseki   =request.POST['menseki']
        nensu     =request.POST['nensu']
        toho      =request.POST['toho']
        #param
        params = {"siki_price" : siki_price
        , "rei_price" : rei_price
        , "menseki" : menseki
        , "nensu"   : nensu
        , "toho"    : toho
        }
        print(params )
        #
        pred =PredPrice()
        model =pred.load_model()
        df = pred.load_data( params )
        price = model.predict(df )
        price_int = np.array( price , np.int32)        
        print( price_int[0] )
#        return HttpResponse('predict-POST')
        return render(request,   'test1/predict_out.html',     # 使用するテンプレート
                  {'price': price_int[0] })         # テンプレートに渡すデータ
    else:
        return HttpResponse('predict')
#
def form_test(request):
    form = MyForm()
    if request.method == 'POST':
        print(request.POST["text"] )
        form = MyForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        if form.is_valid():  # ← 受け取ったデータの正当性確認
            pass  # ← 正しいデータを受け取った場合の処理
        return HttpResponse('form_test_post')
    else:
        return render(request, 'test1/form.html', {
            'form': form,
        })
#
def book_test(request ):
    return render(request, 'test1/book_test.html')