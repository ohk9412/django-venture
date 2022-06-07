from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
import pandas as pd

# Create your views here.


def index(req):
    context = {

    }

    return render(req, "index.html", context=context)


def about(req):
    context = {

    }

    return render(req, "about.html", context=context)


def post(req):
    """
        검색 조회 결과 게시
        1. v_location : 선택한 지역(혹은 권역)
        2. v_property : 선택한 업종
        3. post.html : 결과페이지 전시
    """

    v_location = req.GET.get('location')
    v_property = req.GET.get('property')

    finding = Venture.objects.filter(
        v_region=v_location).filter(v_field=v_property)

    context = {'finding': finding,
               'location': v_location, 'property': v_property}

    return render(req, "post.html", context=context)


def contact(req):
    context = {

    }

    return render(req, "contact.html", context=context)


def database(req):
    """ 
    데이터베이스에 값을 삽입하는 함수

    결과 페이지 : database.html(결과 페이지가 출력되면 정상적으로 DB데이터 삽입이 완료된 것을 의미함)

    """
    context = {

    }

    with open('mysite/db_info.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        for i in range(df.shape[0]):
            Venture.objects.create(
                v_id=df.아이디[i],
                v_address=df.주소[i],
                v_growth=df.기업성장단계[i],
                v_employ=df.신규인력_채용의사[i],
                v_sep=df.구분[i],
                v_predict=df.신규채용_예상인력[i],
                v_doctor=df.신규채용_박사[i],
                v_master=df.신규채용_석사[i],
                v_bachelor=df.신규채용_대졸[i],
                v_college=df.신규채용_전문대졸[i],
                v_high=df.신규채용_고졸이하[i],
                v_region=df.지역[i],
                v_field=df.업종[i])

    return render(req, "database.html", context=context)
