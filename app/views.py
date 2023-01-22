
from ast import Return
from codecs import getencoder
import imp
from pickletools import read_string1
from re import I
import re
from secrets import randbelow
import select
from urllib.request import Request
from urllib.robotparser import RequestRate
from uuid import RESERVED_FUTURE
from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect
from random import randint
from . models import *


from app.models import Customer, UserMaster

# Create your views here.


# Customer home Page render
def IndexPage(request):
     
    if request.method == "POST":

        p_type = request.POST['p_type']
        city = request.POST['city']
       
        
        if city!='' and city is not None and   p_type!='' and p_type is not None : 
            p_data = Property_detail.objects.filter( property_address__icontains = city ,property_type__icontains = p_type)

            return render(request,"app/customer/index.html",{'p_data':p_data})
        
        else:
            if city!='' and city is not None or   p_type!='' and p_type is not None : 
                p_data = Property_detail.objects.filter( property_address__icontains = city ,property_type__icontains = p_type)
                return render(request,"app/customer/index.html",{'p_data':p_data})
                   
    p_data = Property_detail.objects.all()  
    return render(request,"app/customer/index.html",{'p_data':p_data})



def IndexPage2(request): 
    return render(request,"app/customer/index2.html")

# About page render 
def AboutPage(request):
    return render(request,"app/customer/about.html")


# Signup page render 
def SignupPage(request):
    return render(request,"app/customer/signup.html")



# Register user 


def RegisterUser(request):
    # first check the user is Customer or not 
    if request.POST['role'] == "Customer":
        role = request.POST['role'] 
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['pass']
        cpassword  = request.POST['cpass']

        # check the user is allerady exist or not 
        user = UserMaster.objects.filter( email=email )

        if user:
            sms = "User allredy exist"
            return render(request,"app/customer/signup.html",{'msg':sms})

        
        if not request.POST['role'] == "Customer" and not request.POST['role'] == "Agent" :
            sms = "Please Enter your role !"
            return render(request,"app/customer/signup.html",{'msg':sms})

        if not fname:
            sms = "Please Enter your First name !"
            return render(request,"app/customer/signup.html",{'msg':sms})

        if len(fname) < 4:
            sms = "Enter your First name Atlest 4 more charecter"
            return render(request,"app/customer/signup.html",{'msg':sms})

        if not lname:
            sms = "Please Enter your Last name !"
            return render(request,"app/customer/signup.html",{'msg':sms})

        if len(lname) < 4:
            sms = "Enter your Last name Atlest 4 more charecter"
            return render(request,"app/customer/signup.html",{'msg':sms})

        if not email:
            sms = " Please Enter your Email"
            return render(request,"app/customer/signup.html",{'msg':sms})
        
        if not password:
            sms = "Please Enter the password "
            return render(request,"app/customer/signup.html",{'msg':sms})

        if len(password) < 6:
            sms = "Please Enter the password Atleast 6 Charecter! "
            return render(request,"app/customer/signup.html",{'msg':sms})

        
        if not cpassword:
            sms = "Please Enter the Confirm password "
            return render(request,"app/customer/signup.html",{'msg':sms})

        if not password == cpassword:
            sms = " Password and Confirm Password not match !  "
            return render(request,"app/customer/signup.html",{'msg':sms})

        else:
            if password == cpassword:
                otp = randint(111111,999999)
                newuser = UserMaster.objects.create( email=email , password=password , role=role , otp=otp)
                newcust = Customer.objects.create( user_id=newuser, firstname=fname , lastname=lname )
                return render(request,"app/customer/otpverify.html",{'email':email})
            else:
                sms = "Password and confirmt password not match !"
                return render(request,"app/customer/signup.html",{'msg':sms})
            
    else:
        # First check the user is agent or not 
        if request.POST['role'] == "Agent":
            role = request.POST['role'] 
            email = request.POST['email']
            fname = request.POST['fname']
            lname = request.POST['lname']
            password = request.POST['pass']
            cpassword  = request.POST['cpass']

            # check the user is allerady exist or not 
            user = UserMaster.objects.filter( email=email )

            if user:
                sms = "User allredy exist"
                return render(request,"app/customer/signup.html",{'msg':sms})
            
            
            if not request.POST['role'] == "Customer" and not request.POST['role'] == "Agent" :
                sms = "Please Enter your role !"
                return render(request,"app/customer/signup.html",{'msg':sms})

            if not fname:
                sms = "Please Enter your First name !"
                return render(request,"app/customer/signup.html",{'msg':sms})

            if len(fname) < 4:
                sms = "Enter your First name Atlest 4 more charecter"
                return render(request,"app/customer/signup.html",{'msg':sms})

            if not lname:
                sms = "Please Enter your Last name !"
                return render(request,"app/customer/signup.html",{'msg':sms})

            if len(lname) < 4:
                sms = "Enter your Last name Atlest 4 more charecter"
                return render(request,"app/customer/signup.html",{'msg':sms})

            if not email:
                sms = " Please Enter your Email"
                return render(request,"app/customer/signup.html",{'msg':sms})
        
            if not password:
                sms = "Please Enter the password "
                return render(request,"app/customer/signup.html",{'msg':sms})

            if len(password) < 6:
                sms = "Please Enter the password Atleast 6 Charecter! "
                return render(request,"app/customer/signup.html",{'msg':sms})

        
            if not cpassword:
                sms = "Please Enter the Confirm password "
                return render(request,"app/customer/signup.html",{'msg':sms})

            if not password == cpassword:
                sms = " Password and Confirm Password not match !  "
                return render(request,"app/customer/signup.html",{'msg':sms})

                
            else:
                if password == cpassword:
                    otp = randint(111111,999999)
                    newuser = UserMaster.objects.create( email=email , password=password , role=role , otp=otp)
                    newcust = Agent.objects.create( user_id=newuser, firstname=fname , lastname=lname )
                    return render(request,"app/customer/otpverify.html",{'email':email})
                else:
                    sms = "Password and confirmt password not match !"
                    return render(request,"app/customer/signup.html",{'msg':sms})
    
    sms = "First Fillup the Form  !"
    return render(request,"app/customer/signup.html",{'msg':sms})


# otpverify page render
def OtpverifyPage(request):
    return render(request,"app/customer/otpverify.html") 


# Otpverification process
def OtpverificationView(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
  

    # Now Check email is on your database are in or not
    user = UserMaster.objects.get( email=email)

    # If User Are avlaible in your website then chek otp in your database 
    if user:
        # check Otp in your database
        if user.otp == otp:
            sms = "OTP Verification Successfully ."
            return render(request,"app/customer/login.html",{'msg':sms})
        else:
            sms = "OTP Failled"
            return render(request,"app/customer/otpverify.html",{'msg':sms})
    else:
        return render(request,"app/customer/signup.html")
    




# Login page render 
def LoginPage(request):
    return render(request,"app/customer/login.html")


# Login user process
def LoginRegister(request):
    # check register user is Customer or not
    if request.POST['role'] == "Customer":
        email = request.POST['email']
        password = request.POST['pass']


        if not request.POST['role'] == "Customer" and not request.POST['role'] == "Agent" :
            sms = "Please Enter your role !"
            return render(request,"app/customer/login.html",{'msg':sms})

        if not email:
            sms = " Please Enter your Email"
            return render(request,"app/customer/login.html",{'msg':sms})
        
        if not password:
            sms = "Please Enter the password "
            return render(request,"app/customer/login.html",{'msg':sms})

        if len(password) < 6:
            sms = "Please Enter the password Atleast 6 Charecter! "
            return render(request,"app/customer/login.html",{'msg':sms})

        # Check in database user are available or not 
        user = UserMaster.objects.get( email=email )

        # whenever are user available in your database then check 
        if user:
            if user.password == password and user.role == "Customer":
                cust = Customer.objects.get( user_id = user )
                # Create Session 
                request.session['role'] = user.role
                request.session['id'] = user.id
                request.session['firstname'] = cust.firstname
                request.session['lastname'] = cust.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('homepage')
            else:
                sms = "Password incorrect"
                return render(request,"app/customer/login.html",{'msg':sms})
        else:
            sms = "User Does not exist"
            return render(request,"app/customer/login.html",{'msg':sms})
    
    else:
        # check register user is Agent or not
        if request.POST['role'] == "Agent":
            email = request.POST['email']
            password = request.POST['pass']

            if not request.POST['role'] == "Customer" and not request.POST['role'] == "Agent" :
                sms = "Please Enter your role !"
                return render(request,"app/customer/login.html",{'msg':sms})

            if not email:
                sms = " Please Enter your Email"
                return render(request,"app/customer/login.html",{'msg':sms})
        
            if not password:
                sms = "Please Enter the password "
                return render(request,"app/customer/login.html",{'msg':sms})

            if len(password) < 6:
                sms = "Please Enter the password Atleast 6 Charecter! "
                return render(request,"app/customer/login.html",{'msg':sms})

            # Check in database user are available or not 
            user = UserMaster.objects.get( email=email )

            # whenever are user available in your database then check 
            if user:
                if user.password == password and user.role == "Agent":
                    cust = Agent.objects.get( user_id = user )
                    # Create Session 
                    request.session['role'] = user.role
                    request.session['id'] = user.id
                    request.session['firstname'] = cust.firstname
                    request.session['lastname'] = cust.lastname
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return redirect('agenthomepage')
                else:
                    sms = "Password incorrect"
                    return render(request,"app/customer/login.html",{'msg':sms})
            else:
                sms = "User Does not exist"
                return render(request,"app/customer/login.html",{'msg':sms})
    
    sms = "First Fill the form "
    return render(request,"app/customer/login.html",{'msg':sms})
            


# profile Page render 
def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get( user_id=user )
    return render(request,"app/customer/profile.html",{'user':user,'cust':cust})



# Update profile and save the data in database for process
def Updateprofilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    # First check the user is customer or not 
    if user.role == "Customer":
        cust = Customer.objects.get( user_id=user ) 
        cust.contact = request.POST['contact']
        cust.city = request.POST['city']
        cust.state = request.POST['state']
        cust.address = request.POST['add']
        cust.country = request.POST['country']
        cust.biodata = request.POST['biodata']
        cust.dob = request.POST['dob']
        cust.gender = request.POST['gender']
        cust.pincode = request.POST['pincode']
        cust.education = request.POST['education']
        cust.age = request.POST['age']
        cust.website = request.POST['website']
        cust.profile_pic = request.FILES['img']
        cust.save()
        url = f'/profilepage/{pk}' # Formatting url 
        return redirect(url)


# Profileshowpage render and get the particular data 
def ProfileshowPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get( user_id=user )
    return render(request,"app/customer/profileshow.html",{'user':user,'cust':cust})

# Agent data post for detail 
def Agent_grid_data(request):
    p_data = Property_detail.objects.all()
    return render(request,"app/customer/agents-grid.html",{'p_data':p_data})

# Property data render on prperty single pages
def Property_single(request,pk):
        p_data = Property_detail.objects.get(id=pk)
        return render(request,"app/customer/property-single.html",{'p_data':p_data})
    
def Property_agent_single_data(request,pk):
        p_data = Property_detail.objects.get(id=pk)
        all_data = Property_detail.objects.filter(pk=pk)
        return render(request,"app/customer/agent-single.html",{'p_data':p_data,'all_data':all_data})



# Property grid data  Page render
def Property_grid(request):
    if request.method == "POST":

        p_type = request.POST['p_type']
        city = request.POST['city']
       
        
        if city!='' and city is not None and   p_type!='' and p_type is not None : 
            p_data = Property_detail.objects.filter( property_address__icontains = city ,property_type__icontains = p_type)

            return render(request,"app/customer/property-grid.html",{'p_data':p_data})
        
        else:
            if city!='' and city is not None or   p_type!='' and p_type is not None : 
                p_data = Property_detail.objects.filter( property_address__icontains = city ,property_type__icontains = p_type)
                return render(request,"app/customer/property-grid.html",{'p_data':p_data})
                   
    p_data = Property_detail.objects.all()  
    return render(request,"app/customer/property-grid.html",{'p_data':p_data})
  

# Property Apply page render
def Property_apply_page(request,pk):
    user = request.session['id']
    if user:
        cust = Customer.objects.get(user_id=user)
        p_data = Property_detail.objects.get(id=pk)
        return render(request,"app/customer/property-apply.html",{'user':user,'cust':cust,'p_data':p_data})

# Property apply form process definition
def Property_apply_process(request,pk):
    user = request.session['id']
    if user:
  
        cust = Customer.objects.get(user_id = user)
        p_data = Property_detail.objects.get(id=pk)
    
        if cust.profile_pic: 
            customer_image = request.POST['customer_image']
        else:
            customer_image = request.FILES['customer_image']

        need = request.POST['need'] 
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        adhar_card = request.FILES['adhar_card']
        pan_card = request.FILES['pan_card']

        new_apply = Property_apply.objects.create( customer=cust,property=p_data,customer_image=customer_image,
                                                   need=need,min_price=min_price,max_price=max_price,
                                                   adhar_card=adhar_card,pan_card=pan_card )

        sms = "Your request has been sent Successfully  ! Your response will be given soon. "
        return render(request,"app/customer/property-apply.html",{'sms':sms})


# About Page render 
def About_page(request):
    return render(request,"app/customer/about.html")

# Contact page render 
def Contact_page(request):
    return render(request,"app/customer/contact.html")


def Contact_process(request):
    user = request.session['id']
    if user:
        cust = Customer.objects.get(user_id=user)
        subject = request.POST['subject']
        message = request.POST['message']

        con_t = Contact_us.objects.create( customer=cust,subject=subject,message=message )
        sms = "Send message Successfully ."
        return render(request,"app/customer/contact.html",{'sms':sms})



# Sit map page render 
def Site_map(request):
    return render(request,"app/customer/site-map.html")


# Privacy Policy page render 
def Privacy_policy(request):
    return render(request,"app/customer/privacy-policy.html")

# Customer buying list 
def Customer_buying_list(request):
    user = request.session['id']
    cust = Customer.objects.get(user_id=user)
    i = cust.id
    p_data = Property_apply.objects.filter(customer_id = i)
    return render(request,"app/customer/customer_buying.html",{'p_data':p_data})


# Agent property response data 

def Agent_property_response(request):
   

    apr =Property_verification.objects.all()
    return render(request,"app/customer/agent_property_response.html",{'apr':apr})
     



################################### Logout Process #################################
# Logout Customer process
def Customerlogout(request):
    # del is used to delete the session 
    del request.session['email']
    del request.session['password']
    del request.session['role']
    del request.session['id']
    del request.session['firstname']
    del request.session['lastname']
    return redirect('homepage')

# Logout Agent process
def AgentLogout(request):
    del request.session['email']
    del request.session['password']
    
    return redirect('homepage')
   
    

####################################################################################


##################################### Agent Part ##################################3
# Agent home page render 
def Agenthomepage(request):
    return render(request,"app/agent/index.html")

# profile page render
def Agentprofilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    agnt = Agent.objects.get(user_id = user)
    return render(request,"app/agent/profile.html",{'user':user,'agnt':agnt})

# Update Profile process
def Agentupdateprofilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    # First check the user is Agent or not 
    if user.role == "Agent":
        agnt = Agent.objects.get( user_id=user )
        agnt.state = request.POST['state']
        agnt.city = request.POST['city']
        agnt.contact = request.POST['contact']
        agnt.country = request.POST['country']
        agnt.address = request.POST['add']
        agnt.biodata = request.POST['biodata']
        agnt.dob = request.POST['dob']
        agnt.gender = request.POST['gender']
        agnt.pincode = request.POST['pincode']
        agnt.work = request.POST['work']
        agnt.education = request.POST['education']
        agnt.age = request.POST['age']
        agnt.website = request.POST['website']
        agnt.profile_pic = request.FILES['img']
        agnt.save()
        url = f'/agentprofilepage/{pk}' # formatting url 
        return redirect(url)
        

#  Agent Profile show page render
def Agentprofileshow(request,pk):
    user = UserMaster.objects.get(pk=pk)
    agnt = Agent.objects.get(user_id = user)
    return render(request,"app/agent/profile_show.html",{'user':user,'agnt':agnt})

# Agent property post page render 
def Agentpostpropertypage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    agnt = Agent.objects.get(user_id = user)
    return render(request,"app/agent/post-property.html",{'usre':user,'agnt':agnt})



# Insert data in property detail 

def Insertdata_property_detail(request,pk):
    user = UserMaster.objects.get(pk=pk)
    # if check the user is agent user or not 
    if user.role == "Agent":
        agnt = Agent.objects.get( user_id=user )

        agent_firstname = request.POST['agent_firstname']
        agent_lastname = request.POST['agent_lastname']
        agent_email = request.POST['agent_email']
        agent_contact = request.POST['agent_contact']
        agent_city = request.POST['agent_city']
        agent_state = request.POST['agent_state']
        agent_address = request.POST['agent_address']
        agent_country = request.POST['agent_country']
        agent_dob = request.POST['agent_dob']
        agent_gender = request.POST['agent_gender']
        agent_postcode = request.POST['agent_postcode']
        agent_age = request.POST['agent_age']
        agent_education = request.POST['agent_education']
        agent_biodata = request.POST['agent_biodata']
        if agnt.profile_pic:
            agent_profile_pic = request.POST['agent_profile_pic']
        else:
            agent_profile_pic = request.FILES['agent_profile_pic']

        property_name = request.POST['property_name']
        property_address = request.POST['property_address']
        property_description = request.POST['property_description']
      
        property_price = request.POST['property_price']
        property_type = request.POST['property_type']
        property_area_range = request.POST['property_area_range']
        property_beds_seat = request.POST['property_beds_seat']
        property_baths = request.POST['property_baths']
        property_garage = request.POST['property_garage']
        property_balcony = request.POST['property_balcony']
        property_outdoor_kitchen = request.POST['property_outdoor_kitchen']
        property_cable_tv = request.POST['property_cable_tv']
        property_deck = request.POST['property_deck']
        property_tennis_courts = request.POST['property_tennis_courts']
        property_internet = request.POST['property_internet']
        property_parking = request.POST['property_parking']
        property_sun_room = request.POST['property_sun_room']
        property_concreate_flooring = request.POST['property_concreate_flooring']
        property_video = request.FILES['property_video']
        property_floor_plan = request.FILES['property_floor_plan']
        property_pic1 = request.FILES['property_pic1']
        property_pic2 = request.FILES['property_pic2']
        property_pic3 = request.FILES['property_pic3']


        # Inserting the data property_detail

        pd = Property_detail.objects.create(
                                            property_id=agnt,
                                            agent_firstname=agent_firstname,agent_lastname=agent_lastname,
                                             agent_email=agent_email,
                                             agent_contact=agent_contact,agent_city=agent_city,
                                             agent_state=agent_state,agent_address=agent_address,
                                             agent_country=agent_country,agent_dob=agent_dob,
                                             agent_gender=agent_gender,
                                             agent_pincode=agent_postcode,agent_age=agent_age,
                                             agent_education=agent_education,
                                             agent_biodata=agent_biodata,agent_profile_pic=agent_profile_pic,
                                             property_name=property_name,
                                             property_address=property_address,
                                             property_description=property_description,
                                             property_price=property_price,
                                             property_type=property_type,
                                             property_area_range=property_area_range,
                                             property_beds_seat=property_beds_seat,
                                             property_baths=property_baths,
                                             property_garage=property_garage,
                                             property_balcony=property_balcony,
                                             property_outdoor_kitchen=property_outdoor_kitchen,
                                             property_cable_tv=property_cable_tv,property_deck=property_deck,
                                             property_tennis_courts=property_tennis_courts,
                                             property_internet=property_internet,
                                             property_parking=property_parking,
                                             property_sun_room=property_sun_room,
                                             property_concreate_flooring=property_concreate_flooring,
                                             property_video=property_video,
                                             property_floor_plan=property_floor_plan,
                                             property_pic1=property_pic1,property_pic2=property_pic2,property_pic3=property_pic3 )
        
        sms = "Property Post Successfully ."
        return render(request,"app/agent/post-property.html",{'msg':sms})
                            
                                                                                             
# Data for Post property list 
def Data_post_property(request):
        user = request.session['id']
        agnt = Agent.objects.get(user_id=user)
        i = agnt.id
        p_data = Property_detail.objects.filter(property_id=i)
        return render(request,"app/agent/post-property-list.html",{'p_data':p_data})



# Data for Property Apply list 
def Property_apply_list(request):
   
    p_apply = Property_apply.objects.filter()
    return render(request,"app/agent/property-apply-list.html",{'p_apply':p_apply})


# Customer property verification definition

def Customer_property_verification(request,pk):
    cust = Property_apply.objects.get(pk=pk)
    if cust:
        return render(request,"app/agent/agent_verification.html",{'cust':cust})

def Verify_data_customer(request,pk):
    user = request.session['id']
    if user:
        agnt = Agent.objects.get(user_id=user)
        verification = request.POST['verification']
        agnt_new = Property_verification.objects.create( agent=agnt,verification=verification )
        return redirect('property_apply_list')


# About page render     
def Agent_About_page(request):
    return render(request,"app/agent/about.html")

# Agent Site map page rnder 
def Agent_site_map(request):    
    return render(request,"app/agent/site-map.html")    

# Agent Privacy Policy page render 
def Agent_privacy_policy(request):
    return render(request,"app/agent/privacy-policy.html")

# Agent Contact Page render
def Agent_contact_page(request):
    return render(request,"app/agent/contact.html") 


# Agent Contact process 
def Agent_contact_process(request,pk):
    user = request.session['id']
    if user:
        agnt = Agent.objects.get(user_id=user)
        subject = request.POST['subject']
        message = request.POST['message']

        agnt_new = Agent_Contact_us.objects.create( agent=agnt,subject=subject,message=message )
        sms = "Send message Successfully ."
        return render(request,"app/agent/contact.html",{'sms':sms})


######################################### Admin part ###################################

# Admin login page render
def Admin_login_page(request):
    return render(request,"app/admin/login.html")

# Admin login process technique
def Admin_login_process(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "Kishan Maurya" and password == "admin":
        request.session['username']=username
        request.session['password']=password
        return redirect('admin_home_page')
    elif username == "admin" and password =="admin":
        request.session['username']=username
        request.session['password']=password
        return redirect('admin_home_page')
    else:
        sms = "User name and password incorrect"
        return render(request,"app/admin/login.html",{'sms':sms})

# Admin home page render 
def Admin_home_page(request):
    if "username" in request.session and "password" in request.session:
        return render(request,"app/admin/index.html")
    else:
        return redirect('admin_login_page')


# Admin Logout Process 
def Admin_log_out(request):
    del request.session['username']
    del request.session['password']
    return redirect('admin_login_page')


# Admin cusutomer list page render data
def Admin_customer_list(request):
    cust = UserMaster.objects.filter(role="Customer")
    return render(request,"app/admin/customer-list.html",{'cust':cust})

# Admin customer data delete 
def Admin_customer_data_list_delete(request,pk):
    cust_delete = UserMaster.objects.get(pk=pk)
    cust_delete.delete()
    return redirect('admin_customer_page')


# Admin agent list page render data 
def Admin_agent_list(request):
    agnt = UserMaster.objects.filter(role="Agent")
    return render(request,"app/admin/agent-list.html",{'agnt':agnt})

# Admin agent data delete 
def Admin_agent_data_list_delete(request,pk):
    agnt_delete = UserMaster.objects.get(pk=pk)
    agnt_delete.delete()
    return redirect('admin_agent_page')


# Admin Agent contact data 
def Admin_agent_contact_data(request):
    agnt = Agent_Contact_us.objects.all()
    return render(request,"app/admin/agent-contact.html",{'agnt':agnt})

# Admin agent_contact data delete process 
def Admin_agent_contact_data_delete(request,pk):
    agnt_delete = Agent_Contact_us.objects.get(pk=pk)
    agnt_delete.delete()
    return redirect('admin_agent_contact')

    

# Admin Customer contact data 
def Admin_customer_conatct_data(request):
    cust = Contact_us.objects.all()
    return render(request,"app/admin/customer-contact.html",{'cust':cust})

# Admin customer_contact data delete process 
def Admin_customer_contact_data_delete(request,pk):
    cust_delete = Contact_us.objects.get(pk=pk)
    cust_delete.delete()
    return redirect('admin_customer_contact')

# Admin Agent-verification page render with data 
def Admin_agent_verification(request,pk):
    agent = UserMaster.objects.get(pk=pk)
    if agent.role == "Agent":
        return render(request,"app/admin/agent-verification.html",{'agent':agent})

# Admin agent-verification updata the data process
def Admin_agent_verification_update(request,pk):
    agent = UserMaster.objects.get(pk=pk)
    if agent.role=="Agent":
        agent.is_veriFied = request.POST['is_veriFied']
        agent.save()
        return redirect('admin_agent_page')

