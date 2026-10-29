
from django.urls import path
from gym import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('add-membership-plan/',views.AddMembershipPlanView.as_view(), name='add_membership_plan'),
    path('membership-plans/',views.MembershipPlanListView.as_view(),name='membership_plan_list'),
    path('membership-plans/<int:plan_id>/edit/',views.EditMembershipPlanView.as_view(),name='edit_membership_plan'),
    path('membership-plans/<int:plan_id>/delete/',views.DeleteMembershipPlanView.as_view(),name='delete_membership_plan'),

    path('membership-enquiry/',views.MembershipEnquiryView.as_view(),name='membership_enquiry'),
   

    path('add-training-program/',views.AddTrainingProgramView.as_view(),name='add_training_program'),
    path('training-programs/',views.TrainingProgramListView.as_view(),name='training_program_list'),
    path('training-programs/<int:program_id>/edit/',views.EditTrainingProgramView.as_view(),name='edit_training_program'),
    path('training-programs/<int:program_id>/delete/',views.DeleteTrainingProgramView.as_view(),name='delete_training_program'),

    path('add-equipment/',views.AddEquipmentView.as_view(),name='add_equipment'),
    path('equipment/',views.EquipmentListView.as_view(),name='equipment_list'),
    path('equipment/<int:equipment_id>/edit/',views.EditEquipmentView.as_view(),name='edit_equipment'),
    path('equipment/<int:equipment_id>/delete/',views.DeleteEquipmentView.as_view(),name='delete_equipment'),

    path('equipment-enquiry/',views.EquipmentEnquiryView.as_view(),name='equipment_enquiry'),
    path('enquiries/',views.EnquiryListView.as_view(),name='enquiry_list'),
    path('enquiries/<int:enquiry_id>/contacted/',views.MarkEnquiryContactedView.as_view(),name='mark_enquiry_contacted'),


    path('add-supplement/',views.AddSupplementView.as_view(),name='add_supplement'),
    path('supplements/',views.SupplementListView.as_view(),name='supplement_list'),   
    path('supplements/<int:supplement_id>/edit/',views.EditSupplementView.as_view(),name='edit_supplement'),
    path('supplements/<int:supplement_id>/delete/',views.DeleteSupplementView.as_view(),name='delete_supplement'),

    path('owner/personal-training/add/',views.AddPersonalTrainingPackageView.as_view(),name='personal_training_package_add'),
    path('owner/personal-training/',views.PersonalTrainingPackageListView.as_view(),name='personal_training_package_list'),
    path('owner/personal-training/<int:package_id>/edit/',views.EditPersonalTrainingPackageView.as_view(),name='personal_training_package_edit'),
    path('owner/personal-training/<int:package_id>/delete/',views.DeletePersonalTrainingPackageView.as_view(),name='personal_training_package_delete'),

    
]
