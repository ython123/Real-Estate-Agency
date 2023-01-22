from lib2to3.pgen2.token import NAME
from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    # Homepage render url 
    path("",views.IndexPage,name="homepage"),

    path("homepage2/",views.IndexPage,name="homepage2"),
    
    # About page render  url
    path("aboutpage/",views.AboutPage,name="aboutpage"),

    # Singup page url 
    path("signuppage/",views.SignupPage,name="signuppage"),

    # Register user url 
    path("registeruser/",views.RegisterUser,name="registeruser"),


    # Otpverify page render url 
    path("otpverifypage/",views.OtpverifyPage,name="otpverifypage"),

    # Otpverification page url 
    path("otpverificationpage/",views.OtpverificationView,name="otpverificationpage"),

    # Login page url
    path("loginpage/",views.LoginPage,name="loginpage"), 

    # Loginuser process url 
    path("loginuser/",views.LoginRegister,name="loginuser"),

    # Profile page render 
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),

    # Update Profile page render 
    path("updateprofilepage/<int:pk>",views.Updateprofilepage,name="updateprofilepage"),

    # Profile show page render url 
    path("profileshowpage/<int:pk>",views.ProfileshowPage,name="profileshowpage"),

    # Agent data post show data 
    path("agent_grid_data/",views.Agent_grid_data,name="agent_grid_data"),

    # Agent property single data url 
    path("proeperty_single_data/<int:pk>",views.Property_single,name="property_single_data"),

    
    path("property_agent_single_data/<int:pk>",views.Property_agent_single_data,name="property_agent_single_data"),



    # Property APPly page render url 
    path("property_apply_page/<int:pk>",views.Property_apply_page,name="property_apply_page"),

    # Property apply Form process url 
    path("property_apply_process/<int:pk>",views.Property_apply_process,name="property_apply_process"),
    
    # Property grid data page url 
    path("property_grid_data/",views.Property_grid,name="property_grid_data"),

    # About Page render url
    path("about_page/",views.About_page,name="about_page"),

    # Contact Page render url
    path("contact_page/",views.Contact_page,name="contact_page"),

    # Conatct_process url 
    path("contact_process/",views.Contact_process,name="contact_process"),

    # Site Map page render url 
    path("site_map/",views.Site_map,name="site_map"),
    
    # Privacy policy page render url
    path("privacy_policy_page/",views.Privacy_policy,name="privacy_policy"),

    # Customer buying list
    path('customer_buying_list/',views.Customer_buying_list,name="customer_buying_list"),

    # Agent property response data 

    path("agent_property_response/",views.Agent_property_response,name="agent_property_response"),


    #################################### Logout url #############################
    # Logout Customer url 
    path("customerlogout/",views.Customerlogout,name="customerlogout"),

    #Logout Agent url
    path("agentlogout/",views.AgentLogout,name="agentlogout"),

  
    ##############################################################################









    ############################# Agent part url ############################

    # Agent home page url 
    path("agenthomepage/",views.Agenthomepage,name="agenthomepage"),

    # Agent profile page url 
    path("agentprofilepage/<int:pk>",views.Agentprofilepage,name="agentprofilepage"),

    # Agent Update Profile process url 
    path("agentupdateprofilepage/<int:pk>",views.Agentupdateprofilepage,name="agentupdateprofilepage"), 

    # Agent profile show page 
    path("agentprofileshowpage/<int:pk>",views.Agentprofileshow,name="agentprofileshowpage"),

    # Agent post page render url     
    path("agentpostpropertypage/<int:pk>",views.Agentpostpropertypage,name="agentpostpropertypage"),

    # Property post insert data url 
    path("insert_property_post_data/<int:pk>",views.Insertdata_property_detail,name="insert_property_post_data"),

    # Data Post property list url 
    path("data_post_property_list/",views.Data_post_property,name="data_post_property_list"),

    # Data for property post apply list 
    path("property_apply_list/",views.Property_apply_list,name="property_apply_list"),

    # Customer property verification data
    path("customer_property_verification/<int:pk>",views.Customer_property_verification,name="customer_property_verification"),

    # Cutomer verification property 
    path("verify_data_customer/<int:pk>",views.Verify_data_customer,name="verify_data_customer"),

    # Agent About page render url
    path("agent_about_page/",views.Agent_About_page,name="agent_about_page"),

    # Agent Site map page url 
    path("agent_site_map/",views.Agent_site_map,name="agent_site_map"),

    # Agent Privacy policy url 
    path("agent_privacy_policy/",views.Agent_privacy_policy,name="agent_privacy_policy"),

    # Agent Contact Page url
    path("agent_contact_page/",views.Agent_contact_page,name="agent_contact_page"),

    # Agent Contact process url 
    path("agent_contact_process/",views.Agent_contact_process,name="agent_contact_process"),

    ################################# Adminn part url ####################################3

    #Admin page url 
    path("admin_login_page/",views.Admin_login_page,name="admin_login_page"),

    # Admin Login process url 
    path("admin_login_process/",views.Admin_login_process,name="admin_login_process"),

    # Admin home page url 
    path("admin_home_page/",views.Admin_home_page,name="admin_home_page"),

    # Admin Logout process 
    path("admin_log_out/",views.Admin_log_out,name="admin_log_out"),

    # Admin Customer page  data url 
    path("admin_customer_page/",views.Admin_customer_list,name="admin_customer_page"), 

    # Adminn Customer data delete page url
    path("admin_customer_delete_data/<int:pk>",views.Admin_customer_data_list_delete,name="admin_customer_delete_data"),

    # Admin agent page data url 
    path("admin_agent_page/",views.Admin_agent_list,name="admin_agent_page"),

     # Adminn Customer data delete page url
    path("admin_agent_delete_data/<int:pk>",views.Admin_agent_data_list_delete,name="admin_agent_delete_data"),


    # Admin agent contact data url 
    path("admin_agent_contact/",views.Admin_agent_contact_data,name="admin_agent_contact"),

    # Admin agent contact data delete process url 
    path("admin_agent_contact_data_delete/<int:pk>",views.Admin_agent_contact_data_delete,name="admin_agent_contact_data_delete"),

    # Admin customer contact data url 
    path("admin_customer_contact/",views.Admin_customer_conatct_data,name="admin_customer_contact"),

    # Admin customer contact data delete process url 
    path("customer_agent_contact_data_delete/<int:pk>",views.Admin_customer_contact_data_delete,name="admin_customer_contact_data_delete"),


    # Admin verification page render with data  url 
    path("admin_verification/<int:pk>",views.Admin_agent_verification,name="admin_verification"),

    # Admin agent-verification update data url 
    path("admin_agent_verification_update_data/<int:pk>",views.Admin_agent_verification_update,name="admin_agent_verification_update_data"),

   


    

]