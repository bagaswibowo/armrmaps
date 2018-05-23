from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib.auth import logout
import time
from datetime import datetime, timezone
import pytz


config = {
    'apiKey': "AIzaSyC5rT7DmUVrs-dlECDMXBcfMKfE7ItHRZI",
    'authDomain': "maps-1ca28.firebaseapp.com",
    'databaseURL': "https://maps-1ca28.firebaseio.com",
    'projectId': "maps-1ca28",
    'storageBucket': "",
    'messagingSenderId': "43370329320"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
authe = firebase.auth()

def homepage(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def postlogin(request):
    email = request.POST.get('email')
    passwd = request.POST.get('passwd')
    try :
        user = authe.sign_in_with_email_and_password(email, passwd)
    except :
        message = "Invalid Login"
        return render(request,"login.html",{"messag":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"welcome.html", {'e':email})

def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def postsignup(request):
    name = request.POST.get('fullname')
    email = request.POST.get('email')
    passwd = request.POST.get('passwd')

    try:
        user = authe.create_user_with_email_and_password(email,passwd)
        uid = user['localId']
        data = {
        "name" : name,
        "status" : "1",
        }
        db.child("users").child(uid).child("detail").set(data)
    except :
        message = "Cannot Create Your Account"
        return render(request,"signup.html",{"messag":message})

    return render(request,"login.html")

def createreport(request):
    return render(request, "createreport.html")


def post_createreport(request):
    tz = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print ("millis " + str(millis))
    work = request.POST.get('work')
    date = request.POST.get('date')
    descrip = request.POST.get('description')
    data = {
    "work" : work,
    "date" : date,
    "description" : descrip,
    }

    idToken = request.session['uid']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print ("info" + str(a))

    db.child("users").child(a).child("reports").child(millis).set(data)
    name = db.child("users").child(a).child("detail").child("name").get().val()
    return render(request, "welcome.html", {'e':name})

def checkreport(request):
    idToken = request.session['uid']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = db.child('users').child(a).child('reports').shallow().get().val()
    list_time=[]
    for i in timestamps:
        list_time.append(i)

    list_time.sort(reverse=True)


    works = []

    for i in list_time:
        work = db.child('users').child(a).child('reports').child(i).child('work').get().val()
        works.append(work)

    print ("works = " + str(works))

    dates = []
    for i in list_time:
        i = float(i)
        date = datetime.fromtimestamp(i).strftime("%H:%m %D")
        dates.append(date)
    print ("date = " +str(dates))
    # print ("dates" + str(dates))

    posts = zip(list_time,dates,works)

    print (posts)
    return render(request, "checkreport.html",{'posts':posts})

def reportdetail(request,time):
    idToken = request.session['uid']
    a = authe.get_account_info(idToken)
    a = a['users']
    a = a[0]
    a = a['localId']


    descrip = db.child('users').child(a).child('reports').child(time).child('description').get().val()
    date = work = db.child('users').child(a).child('reports').child(time).child('date').get().val()
    work = db.child('users').child(a).child('reports').child(time).child('work').get().val()
    return render(request, "reportdetail.html",{'work':work,'description':descrip,'date':date})



    # millis = millis
    #
    # print (millis)
