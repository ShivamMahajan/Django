from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from .forms import insert #Register 
from .forms import Email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# User Registeration
class register_user_form(forms.ModelForm):
    class Meta:
        model = insert
        fields = ('user_name', 'email_name','password')
     
def register_user(request):
    if request.POST:
        field1_value = request.POST.get('usernamesignup','')
        field2_value = request.POST.get('emailsignup','')
        field3_value = request.POST.get('passwordsignup','')
        instance = insert(user_name=field1_value,email_name=field2_value,password=field3_value)
        instance.save()
        verify_register(request)
    return render(request, 'index3.html')


# Email Send To User after Registeration for Verification
class email_form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Email
        fields = ('subject', 'contact_email', 'content')

def verify_register(request):
    form = register_user_form(request.POST)
    subject = "Welcome To Django"
    email_name = request.POST.get('emailsignup', '')
    fromaddr = "skshivammahajan@gmail.com"
    toaddr = email_name
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body="""<html><head></head>request
                                <body>
        <p>
          <b>
           <a href="http://127.0.0.1:8000/">Verify Email Address</a></b>
        </p>
      </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "missionusa@8")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return render(request, 'index3.html')
    
def get_email(request):
    state = "Send Email To..."

    form = email_form()
     
    return render(request, 'email_form.html',{'state':state, 'form':form})

def get_email_save(request):
    if request.method == 'POST':
        form = email_form(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject', '')
            contact_email = request.POST.get('contact_email', '')
            content = request.POST.get('content', '')
            form.save()
            fromaddr = "skshivammahajan@gmail.com"
            toaddr = contact_email
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = subject
            body="""<html><head></head><body>
                <p><b>  content</b></p>
                <b><a href="www.facebook.com">Verify Email Address</a></b>
                </body></html>"""
            msg.attach(MIMEText(body, 'html'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "missionusa008")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
        object = HttpResponseRedirect('/email/')
    return object    

