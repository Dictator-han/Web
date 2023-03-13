from django.shortcuts import render
from index_app import models
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from utils import wc


# Create your views here.

def index(request):
    return render(request, 'index.html')


def hang(request):
    if request.method == 'POST':
        one = request.POST.get("one")
        two = request.POST.get("two")
        data = models.CiYun.objects.filter(one=one, two=two).values_list('data')[0][0]
        result = wc.get_word_cloud(data)
        company = models.Company.objects.filter(one=one, two=two)
        zhixiao = models.ZhiXiao.objects.filter(one=one, two=two)
        all_data = list(zhixiao.values_list())

        huan_bi = []
        tong_bi = []
        for j in range(2, 8):
            huan = round((float(all_data[2][j]) - float(all_data[1][j])) / float(all_data[1][j]) * 100, 1)
            tong = round((float(all_data[2][j]) - float(all_data[0][j])) / float(all_data[0][j]) * 100, 1)
            huan_bi.append(huan)
            tong_bi.append(tong)

        sum_lst = []
        data_19_21 = []
        for data in all_data:
            now = [float(x) for x in data[2:-2]]
            data_19_21.append(now)
            sum_lst.append(sum(now))
        huan_bi.append(round((sum_lst[2] - sum_lst[1]) / sum_lst[1] * 100, 1))
        tong_bi.append(round((sum_lst[2] - sum_lst[0]) / sum_lst[0] * 100, 1))

        state = []
        for i in range(2, 8):
            uu = []
            for j in all_data:
                uu.append(float(j[i]))
            state.append(uu)
        print(state)
        return render(request, 'hang.html',
                      {"result": result, "company": company, "zhixiao": zhixiao, "sum_lst": sum_lst, "huan_bi": huan_bi,
                       "tong_bi": tong_bi, "data_19_21": data_19_21, "state": state})
    return render(request, 'hang.html')


def cha(request):
    return render(request, 'cha.html')
