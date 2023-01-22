from django.db import models

# Create your models here.
# Master Table 

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active =models.BooleanField(default=True)
    is_veriFied = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

# Customer Table 

class Customer(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=50,default="")
    biodata = models.CharField(max_length=300,default="")
    pincode = models.CharField(max_length=50,default="")
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    website = models.CharField(max_length=150,default="")
    age = models.CharField(max_length=150,default="")
    education = models.CharField(max_length=150,default="")
    profile_pic = models.ImageField(upload_to="app/img/customer")

# Agent table

class Agent(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=50,default="")
    biodata = models.CharField(max_length=300,default="")
    pincode = models.CharField(max_length=50,default="")
    dob = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    work = models.CharField(max_length=300,default="")
    website = models.CharField(max_length=150,default="")
    age = models.CharField(max_length=150,default="")
    education = models.CharField(max_length=150,default="")
    profile_pic = models.ImageField(upload_to="app/img/agent",)


class Property_detail(models.Model):
    property_id = models.ForeignKey(Agent,on_delete=models.CASCADE)
    agent_profile_pic = models.ImageField(upload_to="app/img/agent/profile_pic")
    agent_firstname = models.CharField(max_length=50,default="")
    agent_lastname = models.CharField(max_length=50,default="")
    agent_email  = models.CharField(max_length=150,default="")
    agent_state = models.CharField(max_length=50)
    agent_city = models.CharField(max_length=50)
    agent_contact = models.CharField(max_length=50)
    agent_address = models.CharField(max_length=150)
    agent_country = models.CharField(max_length=50,default="")
    agent_biodata = models.CharField(max_length=300,default="")
    agent_pincode = models.CharField(max_length=50,default="")
    agent_dob = models.CharField(max_length=50,default="")
    agent_gender = models.CharField(max_length=50,default="")
    agent_website = models.CharField(max_length=150,default="")
    agent_age = models.CharField(max_length=150,default="")
    agent_education = models.CharField(max_length=150,default="")
    property_description = models.CharField(max_length=150)
    property_name = models.CharField(max_length=150,default="")
    property_address = models.CharField(max_length=400,default="")
   
    property_price = models.CharField(max_length=150,default="")
    property_type = models.CharField(max_length=150)
    property_location = models.CharField(max_length=150)
    property_area_range = models.CharField(max_length=150)
    property_beds_seat = models.CharField(max_length=150)
    property_baths = models.CharField(max_length=150)
    property_garage = models.CharField(max_length=150)
    property_balcony = models.CharField(max_length=150)
    property_outdoor_kitchen = models.CharField(max_length=150)
    property_cable_tv = models.CharField(max_length=150)
    property_deck = models.CharField(max_length=150)
    property_tennis_courts = models.CharField(max_length=150)
    property_garage = models.CharField(max_length=150)
    property_internet = models.CharField(max_length=150)
    property_parking = models.CharField(max_length=150)
    property_sun_room = models.CharField(max_length=150)
    property_concreate_flooring = models.CharField(max_length=150)
    property_status = models.CharField(max_length=50,default="Sale")
    property_pic1 = models.ImageField(upload_to="app/img/agent/property_pic1")
    property_pic2 = models.ImageField(upload_to="app/img/agent/property_pic2")
    property_pic3 = models.ImageField(upload_to="app/img/agent/property_pic3")
    property_floor_plan = models.ImageField(upload_to="app/img/agent/floor_plan")
    property_video = models.FileField(upload_to="app/video/agent/property_video" ,default="")
    


# Property Apply Table

class Property_apply(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    property = models.ForeignKey(Property_detail,on_delete=models.CASCADE) 
    customer_image = models.ImageField(upload_to="app/image/property_apply/profile_pic")
    need = models.CharField(max_length=300)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    adhar_card = models.FileField(upload_to="app/image/property_apply/adhar_card")
    pan_card = models.FileField(upload_to="app/image/property_apply/pan_card")


# Contact US Table 
class Contact_us(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=300)
    Comment = models.CharField(max_length=500)


# Agent Contact us
class Agent_Contact_us(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=300)

# property_verification data 


class Property_verification(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
   
    verification = models.CharField(max_length=400)

   