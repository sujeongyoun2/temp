from django.shortcuts import render, redirect
from Ihelprapp.models import Forparent, Question1, Forsitter, Member, Mypost
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


import pymysql
dbCon = pymysql.connect('223.194.46.212', 'root', '12345!', 'ihelprdb')


# Create your views here.
def home(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        # context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None

    return render(request, 'homepage.html', context)


def about(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        # context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None
    return render(request, 'about.html', context)


def application(request):
    return render(request, 'application.html')


def forParents(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None

    rsFor = Forparent.objects.all().order_by("-parent_Date")
    context["rsFor"] = rsFor
    return render(request, 'forParents.html', context)


def forSitters(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None

    rsJob = Forsitter.objects.all().order_by("-Date")

    context["rsJob"] = rsJob
    return render(request, 'forSitters.html', context)


def logIn(request):
    return render(request, 'logIn.html')


def messages(request):
    return render(request, 'messages.html')


def messagesBox(request):
    return render(request, 'messagesBox.html')


def myFavorite(request):
    return render(request, 'myFavorite.html')


def myPage(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        # context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None
    return render(request, 'myPage.html', context)


def myPosts(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        # context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None
    mpFor = Mypost.objects.all().order_by("-mp_Date")
    context["mpFor"] = mpFor
    return render(request, 'myPosts.html', context)


def parents_signup(request):
    return render(request, 'parents_signup.html', {})


def postPage(request):
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        # context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None
    return render(request, 'postPage.html', context)


def qna(request):
    print("askCreated")
    context = {}
    if 'member_no' in request.session:
        context["member_no"] = request.session['member_no']
        context["member_name"] = request.session['member_name']

        # context["member_type"] = request.session['member_type']
    else:
        context["member_no"] = None
        context["member_name"] = None

    # db테이블이 모든 데이터가 rsQus 들어감
    rsQus = Question1.objects.all().order_by("-Date")
    # rsQus = Question1.objects.all().order_by("-Title")
    context["rsQus"] = rsQus
    return render(request, 'qna.html', context)


def signUp(request):
    return render(request, 'signUp.html')


def sitters_signup(request):
    return render(request, 'sitters_signup.html')


def viewPost_forParents(request):
    pid = request.GET['p_id']
    print(pid)
    pDetail = Forparent.objects.all().get(b_id=pid)
    return render(request, 'viewPost_forParents.html', {'pDetail': pDetail})


def viewPost(request):
    return render(request, 'viewPost.html')


def askQuestion(request):
    return render(request, 'askQuestion.html')


def postJob(request):
    return render(request, 'postJob.html')


def editMyPost(request):
    mpid = request.GET['mp_id']
    # print(mpid)
    editP = Mypost.objects.all().get(mp_id=mpid)
    return render(request, 'editMyPost.html', {'editP': editP})


def search(request):
    rsFor = Forparent.objects.all().order_by('-parent_Date')
    q = request.POST.get('q', "")
    if q:
        rsFor = rsFor.filter(parent_Title__icontains=q)
        return render(request, 'forParents.html', {'rsFor': rsFor, 'q': q})


def deleteMyPost(request):
    mpid = request.GET['mp_id']
    print(mpid)
    deleteP = Mypost.objects.all().get(mp_id=mpid).delete()
    mpFor = Mypost.objects.all().order_by("-mp_Date")
    return render(request, 'myPosts.html', {'mpFor': mpFor})


@csrf_exempt
def askCreated(request):
    context = {}
    btitle = request.GET['title_b']
    rsQus = Question1.objects.create(Title=btitle, Date=datetime.now())
    context["result"] = "Successfully Post Question"

    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def postJobwant(request):
    context = {}
    print("=========")
    print(context)
    print("=========")
    parentName = request.GET['parent_Name']
    parentTitle = request.GET['parent_Title']
    parentLocation = request.GET['parent_Location']
    parentPayrate = request.GET['parent_Payrate']
    parentNote = request.GET['parent_Note']
    print("=======1==")
    parentService = request.GET['parent_Service']
    print("======2===")
    parentWorkperiod = request.GET['parent_Workperiod']
    parentTimefrom = request.GET['parent_Timefrom']
    parentWorkto = request.GET['parent_Workto']
    parentGender = request.GET['parent_Gender']
    print("=========")
    print(parentService)
    # 부모
    rsFor = Forparent.objects.create(
        parent_Name=parentName, parent_Title=parentTitle, parent_Location=parentLocation, parent_Payrate=parentPayrate, parent_Note=parentNote, parent_Service=parentService, parent_Workperiod=parentWorkperiod, parent_Timefrom=parentTimefrom, parent_Workto=parentWorkto, parent_Gender=parentGender, parent_Date=datetime.now())

    context["result"] = "Success!"
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def postJobOpening(request):
    context = {}

    bname = request.GET['name_b']
    btitle = request.GET['title_b']
    blocation = request.GET['location_b']

    # 시터
    rsJob = Forsitter.objects.create(
        Name=bname, Title=btitle, Location=blocation, Date=datetime.now())

    context["result"] = "Post Successfully"
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def member_insert(request):
    context = {}

    memberid = request.GET['member_id']
    memberpwd = request.GET['member_pwd']
    membername = request.GET['member_name']
    memberemail = request.GET['member_email']

    membertype = request.GET['member_type']

    rs = Member.objects.create(member_id=memberid, member_pwd=memberpwd,
                               member_name=membername, member_email=memberemail, member_type=membertype,
                               usage_flag='1', register_date=datetime.now())

    context["result"] = "Successfull"
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def member_login(request):
    context = {}
    memberid = request.GET['member_id']
    memberpwd = request.GET['member_pwd']

    # print("====================")
    # print(memberid)
    # print("====================")
    # 섹션 자기만의 섹션이 있는거다
    if 'member_no' in request.session:
        # context["flag"] = "1"
        context["result"] = 'Already Log in'
    else:

        rs = Member.objects.filter(member_id=memberid, member_pwd=memberpwd)

        if(len(rs)) == 0:
            # context["flag"] = "1"
            context["result"] = "NOT Log in try again"
        else:

            rsMember = Member.objects.get(
                member_id=memberid, member_pwd=memberpwd,)
            memberno = rsMember.member_no
            membername = rsMember.member_name

            rsMember.access_latest = datetime.now()
            rsMember.save()

            request.session['member_no'] = memberno
            request.session['member_name'] = membername

            request.session['member_type'] = rsMember.member_type

            # context["flag"] = "0"
            # context["result"] = "Successfull Log in"

    return JsonResponse(context, content_type="application/json")


def log_out(request):
    context = {}
    request.session.flush()
    return redirect("/")
