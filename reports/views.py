from unittest import result
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector
from .models import rep





def registration_stu(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reviewreports"
        )

        mycursor = mydb.cursor() 
        team_id=request.POST['team_id']
        team_members=request.POST['team_members']
        project_title=request.POST['project_title']
        ppt_link=request.POST['ppt_link']
        mycursor.execute("insert into project_info(team_id,team_members,project_title,ppt_link)values('"+team_id+"','"+team_members+"','"+project_title+"','"+ppt_link+"')")
        mydb.commit()
        return redirect('final_report')
    else:
        return render(request,'registration_stu.html')
def registration_faculty(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reviewreports"
        )

        mycursor = mydb.cursor() 
        team_id=request.POST['team_id']
        Date_1streview=request.POST['Date_1streview']
        first_review_grade=request.POST['first_review_grade']
        per_first_completed=request.POST['per_first_completed']
        Date_2ndreview=request.POST['Date_2ndreview']
        second_review_grade=request.POST['second_review_grade']
        per_sec_completed=request.POST['per_sec_completed']
        overall_status=request.POST["overall_status"]

        
        mycursor.execute("insert into reviews_info(team_id,Date_1st_review,first_review_grade,per_fir_completed,Date_2nd_review,second_review_grade,per_sec_completed,overall_status)values('"+team_id+"','"+Date_1streview+"','"+first_review_grade+"','"+per_first_completed+"','"+Date_2ndreview+"','"+second_review_grade+"','"+per_sec_completed+"','"+overall_status+"')")
        mydb.commit()
        return redirect('registration_faculty')
    else:
        return render(request,'registration_faculty.html')
def login_fac(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reviewreports"
        )
    
        mycursor = mydb.cursor()

        faculty_id=request.POST['faculty_id']
        password=request.POST['password']
        mycursor.execute("select * from faculty_info where faculty_id='"+faculty_id+"' and password='"+password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            return redirect('registration')

        else:
            return render(request,'login_fac.html',{'status':'Invalid Credentials'}) 

    else:
        return render(request,'login_fac.html')
def login_stu(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reviewreports"
        )
    
        mycursor = mydb.cursor()

        student_id=request.POST['student_id']
        password=request.POST['password']
        mycursor.execute("select * from student_info where student_id='"+student_id+"' and password='"+password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            return redirect('registration_stu')

        else:
            return render(request,'login_stu.html',{'status':'Invalid Credentials'}) 

    else:
        return render(request,'login_stu.html')
def final_report(request):
    if(request.method=="POST"):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reviewreports"
        )    
        mycursor = mydb.cursor()
        s=request.POST['team_id']
        
        sql_query = """
           SELECT 
    p.team_id,
    p.team_members,
    p.project_title,
    p.ppt_link,
    COALESCE(r1.review1_date, 'Not available') AS Date_1st_review,
    COALESCE(r1.grade1, 'Not available') AS first_review_grade,
    COALESCE(r1.percentage1, 'Not available') AS per_fir_completed,
    COALESCE(r1.remarks1, 'Not available') AS remarks1,
    COALESCE(r2.review2_date, 'Not available') AS Date_2nd_review,
    COALESCE(r2.grade2, 'Not available') AS second_review_grade,
    COALESCE(r2.percentage2, 'Not available') AS per_sec_completed,
    COALESCE(r2.remarks2, 'Not available') AS remarks2,
    COALESCE(r3.review3_date, 'Not available') AS Date_3rd_review,
    COALESCE(r3.grade3, 'Not available') AS third_review_grade,
    COALESCE(r3.percentage3, 'Not available') AS per_third_completed,
    COALESCE(r3.remarks3, 'Not available') AS remarks3
FROM 
    project_info p
LEFT JOIN 
    review1 r1 ON p.team_id = r1.team_id
LEFT JOIN 
    review2 r2 ON p.team_id = r2.team_id
LEFT JOIN 
    review3 r3 ON p.team_id = r3.team_id
WHERE 
    p.team_id = %s;


        """
        mycursor.execute(sql_query,(s,))
        result=mycursor.fetchall()
        reviewdetails=[]
        for x in result:
            Rep=rep()
            Rep.team_id=x[0]
            Rep.team_members=x[1]
            Rep.project_title=x[2]
            Rep.ppt_link=x[3]
            Rep.Date_1st_review=x[4]
            Rep.first_review_grade=x[5]
            Rep.per_fir_completed=x[6]
            Rep.remarks1=x[7]
            Rep.Date_2nd_review=x[8]
            Rep.second_review_grade=x[9]
            Rep.per_sec_completed=x[10]
            Rep.remarks2=x[11]
            Rep.Date_3rd_review=x[12]
            Rep.third_review_grade=x[13]
            Rep.per_thr_completed=x[14]
            Rep.remarks3=x[15]
            reviewdetails.append(Rep)
        return render(request,'final_report.html',{'freports':reviewdetails})
    
    else:
        return render(request, 'final_report.html')
def final_report_fac(request):
    if(request.method=="POST"):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reviewreports"
        )    
        mycursor = mydb.cursor()
        '''s=request.POST['college']'''
        
        sql_query = """
            SELECT 
    pi.team_id,
    pi.team_members,
    pi.project_title,
    pi.ppt_link,
    r1.review1_date,
    r1.percentage1,
    r1.grade1,
    r1.remarks1,
    r2.review2_date,
    r2.percentage2,
    r2.grade2,
    r2.remarks2,
    r3.review3_date,
    r3.percentage3,
    r3.grade3,
    r3.remarks3
FROM 
    project_info pi
JOIN 
    review1 r1 ON pi.team_id = r1.team_id
JOIN 
    review2 r2 ON pi.team_id = r2.team_id
JOIN 
    review3 r3 ON pi.team_id = r3.team_id;

        """
        mycursor.execute(sql_query)
        result=mycursor.fetchall()
        reviewdetails=[]
        for x in result:
            Rep=rep()
            Rep.team_id=x[0]
            Rep.team_members=x[1]
            Rep.project_title=x[2]
            Rep.ppt_link=x[3]
            Rep.Date_1st_review=x[4]
            Rep.first_review_grade=x[5]
            Rep.per_fir_completed=x[6]
            Rep.remarks1=x[7]
            Rep.Date_2nd_review=x[8]
            Rep.second_review_grade=x[9]
            Rep.per_sec_completed=x[10]
            Rep.remarks2=x[11]
            Rep.Date_3rd_review=x[12]
            Rep.third_review_grade=x[13]
            Rep.per_thr_completed=x[14]
            Rep.remarks3=x[15]
            reviewdetails.append(Rep)
        return render(request,'final_report_fac.html',{'freports':reviewdetails})
    
    else:
        return render(request, 'final_report_fac.html')
    # Assuming you have a model named 'rep' defined in your models.py file


def registration(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="reviewreports"
        )
        mycursor = mydb.cursor()
        s = request.POST['team_id']
        
        sql_query = """
        SELECT 
    p.team_id,
    p.team_members,
    p.project_title,
    p.ppt_link,
    COALESCE(r1.review1_date, 'Not available') AS Date_1st_review,
    COALESCE(r1.grade1, 'Not available') AS first_review_grade,
    COALESCE(r1.percentage1, 'Not available') AS per_fir_completed,
    COALESCE(r1.remarks1, 'Not available') AS remarks1,
    COALESCE(r2.review2_date, 'Not available') AS Date_2nd_review,
    COALESCE(r2.grade2, 'Not available') AS second_review_grade,
    COALESCE(r2.percentage2, 'Not available') AS per_sec_completed,
    COALESCE(r2.remarks2, 'Not available') AS remarks2,
    COALESCE(r3.review3_date, 'Not available') AS Date_3rd_review,
    COALESCE(r3.grade3, 'Not available') AS third_review_grade,
    COALESCE(r3.percentage3, 'Not available') AS per_third_completed,
    COALESCE(r3.remarks3, 'Not available') AS remarks3
FROM 
    project_info p
LEFT JOIN 
    review1 r1 ON p.team_id = r1.team_id
LEFT JOIN 
    review2 r2 ON p.team_id = r2.team_id
LEFT JOIN 
    review3 r3 ON p.team_id = r3.team_id
WHERE 
    p.team_id = %s;


        """
        mycursor.execute(sql_query,(s,))
        result=mycursor.fetchall()
        reviewdetails=[]
        for x in result:
            Rep=rep()
            Rep.team_id=x[0]
            Rep.team_members=x[1]
            Rep.project_title=x[2]
            Rep.ppt_link=x[3]
            Rep.Date_1st_review=x[4]
            Rep.first_review_grade=x[5]
            Rep.per_fir_completed=x[6]
            Rep.remarks1=x[7]
            Rep.Date_2nd_review=x[8]
            Rep.second_review_grade=x[9]
            Rep.per_sec_completed=x[10]
            Rep.remarks2=x[11]
            Rep.Date_3rd_review=x[12]
            Rep.third_review_grade=x[13]
            Rep.per_thr_completed=x[14]
            Rep.remarks3=x[15]
            reviewdetails.append(Rep)
        return render(request,'registration.html',{'freports':reviewdetails})
    
    else:
        return render(request, 'registration.html')
def submit_review1(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="reviewreports"
        )
        mycursor = mydb.cursor()

        team_id = request.POST['team_id_1']
        review1_date = request.POST['review1_date']
        percentage1 = request.POST['percentage1']
        grade1 = request.POST['grade1']
        remarks1 = request.POST['remarks1']

        sql_query = """INSERT INTO review1 (team_id, review1_date, percentage1, grade1, remarks1) 
                       VALUES (%s, %s, %s, %s, %s)"""
        review1_data = (team_id, review1_date, percentage1, grade1, remarks1)
        mycursor.execute(sql_query, review1_data)
        mydb.commit()
        return redirect('registration')  # Redirect to the registration page after submission
    else:
        return HttpResponse("Invalid request")

def submit_review2(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="reviewreports"
        )
        mycursor = mydb.cursor()

        team_id = request.POST['team_id_2']
        review2_date = request.POST['review2_date']
        percentage2 = request.POST['percentage2']
        grade2 = request.POST['grade2']
        remarks2 = request.POST['remarks2']

        sql_query = """INSERT INTO review2 (team_id, review2_date, percentage2, grade2, remarks2) 
                       VALUES (%s, %s, %s, %s, %s)"""
        review2_data = (team_id, review2_date, percentage2, grade2, remarks2)
        mycursor.execute(sql_query, review2_data)
        mydb.commit()
        return redirect('registration')
    else:
        return HttpResponse("Invalid request")

def submit_review3(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="reviewreports"
        )
        mycursor = mydb.cursor()

        team_id = request.POST['team_id_3']
        review3_date = request.POST['review3_date']
        percentage3 = request.POST['percentage3']
        grade3 = request.POST['grade3']
        remarks3 = request.POST['remarks3']

        sql_query = """INSERT INTO review3 (team_id, review3_date, percentage3, grade3, remarks3) 
                       VALUES (%s, %s, %s, %s, %s)"""
        review3_data = (team_id, review3_date, percentage3, grade3, remarks3)
        mycursor.execute(sql_query, review3_data)
        mydb.commit()
        return redirect('registration')
    else:
        return HttpResponse("Invalid request")

