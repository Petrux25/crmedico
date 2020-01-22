from django.shortcuts import render, redirect
from app_users.models import MedService
from django.contrib.auth.models import User
from .models import Time, Appointments
from django.http import JsonResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create(request, med_id):
    med = User.objects.filter(username=med_id)[0]

    return render(request, "create.html", {"med": med, "username":med.username})


def get_times(request):
    times = Time.objects.exclude(appointment__date=request.POST['date'])
    times = list(map(to_time, times))
    
    return JsonResponse(times,safe=False)


def to_time(time):
    print(time)
    return {"id":time.id, "time":time.time}

def save_appointment(request):
    current_user=request.user
    medId=request.POST['usr']
    med = User.objects.filter(username=medId)[0]
    med_email = User.objects.filter(username=medId).values('email').first()['email']
    print(med_email)
    date=request.POST['date']
    time=Time.objects.get(id=request.POST['time'])
    appointment=Appointments(date=date, time=time,med=med,patient=current_user)
    appointment.save()
    send_email(current_user.email, 'Recordatorio de Cita','Estimado usuario, se le recuerda que usted tiene una cita agendada para el día '+date+' con el doctor '+med.username)
    send_email(med_email, 'Recordatorio de Cita', 'Estimado Dr., se le recuerda que usted tiene una cita agendada con el paciente '+str(current_user)+ 'el día '+date)
    return redirect('users:login')

def send_email(user_email, subject, message):
    sender_email_address = 'crmedico.notificaciones@gmail.com'
    sender_email_password = 'crmedico2020'
    receiver_email_address = user_email

    email_subject_line = subject

    msg = MIMEMultipart()
    msg['From'] = sender_email_address
    msg['To'] = receiver_email_address
    msg['Subject'] = email_subject_line
    email_body = message
    msg.attach(MIMEText(email_body, 'plain'))

    email_content = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_email_address, sender_email_password)
    server.sendmail(sender_email_address, receiver_email_address, email_content)
    server.quit()
    return "todo bien"


