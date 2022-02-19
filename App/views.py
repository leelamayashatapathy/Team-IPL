from django.contrib import messages
from logging import exception
from django.http import HttpResponse
import json
from django.shortcuts import render

# Create your views here.

def index(request):
    with open("team.json","r") as f1:
        v1=json.load(f1)
        for i in v1:
            print(i.get("Team_Id"))

    with open("player.json","r") as fi:
        data5=json.load(fi)
        for i in data5:
            if i.get("Team_n") in v1:
                print(i.get("Team_n").count())

        
        
    #     [csk,dc,kxip,kkr,mi,rr,rcb,srh]
        
    #     for i in data5:
    #         if i.get('Team_n')=="csk":
    #             csk+=1
    #         elif i.get('Team_n')=="dc":
    #             dc+=1
    #         elif i.get('Team_n')=="kxip":
    #             kxip+=1
    #         elif i.get('Team_n')=="kkr":
    #             kkr+=1
    #         elif i.get('Team_n')=="mi":
    #             mi+=1
    #         elif i.get('Team_n')=="rr":
    #             rr+=1
    #         elif i.get('Team_n')=="rcb":
    #             rcb+=1
    #         elif i.get('Team_n')=="srh":
    #             srh+=1
            

    # with open("newteam.json","r") as new:
    #     db=json.load(new)
        
               
    return render(request,"index.html",{"context1":v1})

       

def updateplayer(request):
    if request.method == 'POST':
        print("method is post")
        pid1=request.POST['pid']
        name=request.POST['pname']
        dob=request.POST['dob']
        Price=request.POST['price']
        pstatus=request.POST['status']
        print(pid1)
        country=request.POST['country']
        role=request.POST['role']
        teamid=request.POST['teamid']
        img=request.POST['img']
        print(pid1)
        v={"Player_Id":pid1,"Player_Name":name,"DOB":dob,"Price":Price,
        "Playing_Status":pstatus,"Country":country,"Is_Umpire":"Null","Team_n":teamid,"Role":role,
            "Image_Id":img
                    }
        with open("player.json","r") as f3:
            data=json.load(f3)
        data.append(v)
        with open("player.json","w") as f3:
            json.dump(data,f3,indent=10)
    return render(request,"updateplayer.html")



def updateteam(request):
    if request.method == 'POST':
        print("method is post")
        tid1=request.POST['tid']
        tname=request.POST['tname']
        tsc=request.POST['sc']
        tbat=request.POST['tbat']
        tball=request.POST['tbal']
        
        trophy=request.POST['twon']
        logo=request.POST['timg']
        totalplayer=request.POST['tplay']
        # img=request.POST['img']
        
        v={"Team_Id":tid1,"Team_Name":tname,"Team_Short_Code":tsc,"Top_Batsman":tbat,
        "Top_Bowler":tball,"Trophy_Won":trophy,"totalplayer":totalplayer,"Image_Id":logo
                    }
        with open("team.json","r") as f3:
            data=json.load(f3)
        data.append(v)
        with open("team.json","w") as f3:
            json.dump(data,f3,indent=10)
    return render(request,"updateteam.html")





def search(request):
    if request.method=='POST':
        query1=request.POST['query']
    
        if query1!="":
            v=query1.lower()
            print(v)
            with open("player.json","r") as f4:
                data=json.load(f4)
                for i in data:
                    m=i.get("Team_Short_Code")
                    print(m)
                    return render(request,"search.html",{"datavalue":data,"query1":v})
        else:
            a=" OOPS!:( ,Enter team short code to get result "
            return render(request,"search.html",{"message":a})

def teamdetails(request,id):
    with open("player.json","r") as d:
        mk=json.load(d)
        print(id)
    return render(request,"teamdetail.html",{"context":mk,"team":id})


def playerdetails(request,id):
    print(id)
    with open("player.json","r") as pd:
        pdetail=json.load(pd)

    return render(request,"playerdetail.html",{"player":pdetail,"pid":id})

            
            

            

    

    
