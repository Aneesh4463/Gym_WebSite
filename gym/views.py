
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import MembershipPlan,TrainingProgram,Equipment,Enquiry,Supplement,PersonalTrainingPackage
from .forms import MembershipPlanForm,TrainingProgramForm,EquipmentForm,EnquiryForm,SupplementForm,PersonalTrainingPackageForm
from django.utils.safestring import mark_safe
from accounts.views import OwnerRequiredMixin



class HomeView(View):

    def get(self, request, *args, **kwargs):

        # Get active membership plans
        plans = MembershipPlan.objects.filter(is_active=True)

        # Get active training programs
        programs = TrainingProgram.objects.filter(is_active=True)

        # Get available equipment
        equipment = Equipment.objects.filter(is_available=True)

        # Get available supplements
        supplements = Supplement.objects.filter(is_available=True)

        # Get active personal training packages
        personal_training_packages = PersonalTrainingPackage.objects.filter(
            is_active=True
        )
        # print("PT PACKAGES:", list(personal_training_packages.values("package_name","is_active")))

        # Convert personal training benefits into a list
        for package in personal_training_packages:
            package.benefit_list = [
                benefit.strip()
                for benefit in package.benefits.splitlines()
                if benefit.strip()
            ]

        # Convert membership benefits into a list
        for plan in plans:
            plan.benefit_list = [
                benefit.strip()
                for benefit in plan.benefits.splitlines()
                if benefit.strip()
            ]

        # Send all data to the homepage
        context = {
            'plans': plans,
            'programs': programs,
            'equipment': equipment,
            'supplements': supplements,
            'personal_training_packages': personal_training_packages,
        }

        return render(request, 'gym/home.html', context)



class AddMembershipPlanView(OwnerRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        form = MembershipPlanForm()

        return render(request,'gym/add_membership_plan.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = MembershipPlanForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('add_membership_plan')
        
        return render(request,'gym/add_membership_plan.html',{'form': form})


class MembershipPlanListView(OwnerRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        plans = MembershipPlan.objects.all()

        return render(request,'gym/membership_plan_list.html',{'plans': plans})



class EditMembershipPlanView(OwnerRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        plan_id = kwargs.get('plan_id')

        plan = MembershipPlan.objects.get(id=plan_id)

        form = MembershipPlanForm(instance=plan)

        return render(request,'gym/edit_membership_plan.html',{'form': form, 'plan': plan})

    def post(self, request, *args, **kwargs):

        plan_id = kwargs.get('plan_id')

        plan = MembershipPlan.objects.get(id=plan_id)

        form = MembershipPlanForm(request.POST,instance=plan)

        if form.is_valid():

            form.save()

            return redirect('membership_plan_list')

        return render(request,'gym/edit_membership_plan.html',{'form': form, 'plan': plan})




class DeleteMembershipPlanView(OwnerRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        plan_id = kwargs.get('plan_id')

        plan = MembershipPlan.objects.get(id=plan_id)

        return render(request,'gym/delete_membership_plan.html',{'plan': plan})

    def post(self, request, *args, **kwargs):

        plan_id = kwargs.get('plan_id')

        plan = MembershipPlan.objects.get(id=plan_id)

        plan.delete()

        return redirect('membership_plan_list')



# traning..............



class AddTrainingProgramView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        form = TrainingProgramForm()

        return render(request,'gym/add_training_program.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = TrainingProgramForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('training_program_list')

        return render(request,'gym/add_training_program.html',{'form': form})


class TrainingProgramListView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        programs = TrainingProgram.objects.all()

        return render(request,'gym/training_program_list.html',{'programs': programs})



class EditTrainingProgramView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        program_id = kwargs.get('program_id')

        program = TrainingProgram.objects.get(id=program_id)

        form = TrainingProgramForm(instance=program)

        return render(request,'gym/edit_training_program.html',{'form': form, 'program': program})

    def post(self, request, *args, **kwargs):

        program_id = kwargs.get('program_id')

        program = TrainingProgram.objects.get(id=program_id)

        form = TrainingProgramForm(request.POST,instance=program)

        if form.is_valid():

            form.save()

            return redirect('training_program_list')

        return render(request,'gym/edit_training_program.html',{'form': form, 'program': program})



class DeleteTrainingProgramView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        program_id = kwargs.get('program_id')

        program = TrainingProgram.objects.get(id=program_id)

        return render(request,'gym/delete_training_program.html',{'program': program})

    def post(self, request, *args, **kwargs):

        program_id = kwargs.get('program_id')

        program = TrainingProgram.objects.get(id=program_id)

        program.delete()

        return redirect('training_program_list')


# equpi.............


class AddEquipmentView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        form = EquipmentForm()

        return render(request,'gym/add_equipment.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = EquipmentForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('equipment_list')

        return render(request,'gym/add_equipment.html',{'form': form})


class EquipmentListView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        equipment_list = Equipment.objects.all().order_by('-id')

        return render(request,'gym/equipment_list.html',{'equipment_list': equipment_list})



class EditEquipmentView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        equipment_id = kwargs.get('equipment_id')

        equipment = Equipment.objects.get(id=equipment_id)

        form = EquipmentForm(instance=equipment)

        return render(request,'gym/edit_equipment.html',{'form': form,'equipment': equipment,})

    def post(self, request, *args, **kwargs):

        equipment_id = kwargs.get('equipment_id')

        equipment = Equipment.objects.get(id=equipment_id)

        form = EquipmentForm(request.POST,request.FILES,instance=equipment)

        if form.is_valid():

            form.save()

            return redirect('equipment_list')

        return render(request,'gym/edit_equipment.html',{'form': form,'equipment': equipment,})



class DeleteEquipmentView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        equipment_id = kwargs.get('equipment_id')

        equipment = Equipment.objects.get(id=equipment_id)

        return render(request,'gym/delete_equipment.html',{'equipment': equipment})

    def post(self, request, *args, **kwargs):

        equipment_id = kwargs.get('equipment_id')

        equipment = Equipment.objects.get(id=equipment_id)

        equipment.delete()

        return redirect('equipment_list')


# enquiery...............


class EquipmentEnquiryView(View):

    def get(self, request, *args, **kwargs):

        item_name = request.GET.get('item', '')

        form = EnquiryForm(initial={'item_name': item_name})

        return render(request,'gym/equipment_enquiry.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = EnquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return render(request,'gym/equipment_enquiry.html',{'form': EnquiryForm(),'success': True})

        return render(request,'gym/equipment_enquiry.html',{'form': form})



class EnquiryListView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        enquiries = Enquiry.objects.all().order_by('-created_at')

        equipment_names = {name.strip() for name in Equipment.objects.values_list('name', flat=True)}

        supplement_names = {name.strip() for name in Supplement.objects.values_list('name', flat=True)}

        membership_enquiries = []
        equipment_enquiries = []
        supplement_enquiries = []

        for enquiry in enquiries:

            item_name = (enquiry.item_name or '').strip()

            if item_name in equipment_names:
                equipment_enquiries.append(enquiry)

            elif item_name in supplement_names:
                supplement_enquiries.append(enquiry)

            else:
                membership_enquiries.append(enquiry)

        context = {
            'enquiry_sections': [
                ('Membership Enquiries', membership_enquiries),
                ('Equipment Enquiries', equipment_enquiries),
                ('Supplement Enquiries', supplement_enquiries),
            ]
        }

        return render(request, 'gym/enquiry_list.html', context)


class MarkEnquiryContactedView(OwnerRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        enquiry_id = kwargs.get('enquiry_id')

        enquiry = Enquiry.objects.get(id=enquiry_id)
        enquiry.is_contacted = True
        enquiry.save(update_fields=['is_contacted'])

        return redirect('enquiry_list')


# supplyment


class AddSupplementView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        form = SupplementForm()

        return render(request,'gym/add_supplement.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = SupplementForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('supplement_list')

        return render(request,'gym/add_supplement.html',{'form': form})



class SupplementListView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        supplements = Supplement.objects.all().order_by('-id')

        return render(request,'gym/supplement_list.html',{'supplements': supplements})



class EditSupplementView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        supplement_id = kwargs.get('supplement_id')

        supplement = get_object_or_404(Supplement,id=supplement_id)

        form = SupplementForm(instance=supplement)

        return render(request,'gym/edit_supplement.html',{'form': form,'supplement': supplement})

    def post(self, request, *args, **kwargs):

        supplement_id = kwargs.get('supplement_id')

        supplement = get_object_or_404(Supplement,id=supplement_id)

        form = SupplementForm(request.POST,request.FILES,instance=supplement)

        if form.is_valid():

            form.save()

            return redirect('supplement_list')

        return render(request,'gym/edit_supplement.html',{'form': form,'supplement': supplement})



class DeleteSupplementView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        supplement_id = kwargs.get('supplement_id')

        supplement = get_object_or_404(Supplement,id=supplement_id)

        return render(request,'gym/delete_supplement.html',{'supplement': supplement})

    def post(self, request, *args, **kwargs):

        supplement_id = kwargs.get('supplement_id')

        supplement = get_object_or_404(Supplement,id=supplement_id)

        supplement.delete()

        return redirect('supplement_list')




from django.contrib import messages

class MembershipEnquiryView(View):

    def get(self, request):
        return redirect('home')

    def post(self, request):
        name = request.POST.get('full_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        enquiry_type = request.POST.get('enquiry_type', 'membership').strip()
        selected_item = request.POST.get('selected_item', '').strip()

        if not name or not phone or not selected_item:
            messages.error(request,'Please enter your name, phone and selected item.')
            return redirect('home')

       

        form_data = {
            'name': name,
            'phone': phone,
            'email': email or 'noemail@example.com',
            'item_name': selected_item,
            'message': request.POST.get('message', '').strip(),

        }

        form = EnquiryForm(form_data)

        if form.is_valid():
            form.save()
            messages.success(request,'Your enquiry was submitted successfully!')
        else:
            messages.error(request,'Please enter valid enquiry details.')

        return redirect('home')



class AddPersonalTrainingPackageView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        form = PersonalTrainingPackageForm()

        return render(request,'gym/add_personal_training_package.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = PersonalTrainingPackageForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('personal_training_package_list')

        return render(request,'gym/add_personal_training_package.html',{'form': form})



class PersonalTrainingPackageListView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        packages = PersonalTrainingPackage.objects.all().order_by('-id')

        context = {

            'packages': packages
        }

        return render(request,'gym/personal_training_package_list.html',context)


class EditPersonalTrainingPackageView(OwnerRequiredMixin, View):

    def get(self, request, package_id):

        package = get_object_or_404(PersonalTrainingPackage,id=package_id)

        form = PersonalTrainingPackageForm(instance=package)

        return render(request,'gym/edit_personal_training_package.html',{'form': form, 'package': package})

    def post(self, request, package_id):

        package = get_object_or_404(PersonalTrainingPackage,id=package_id)

        form = PersonalTrainingPackageForm(request.POST,instance=package)

        if form.is_valid():

            form.save()

            return redirect('personal_training_package_list')

        return render(request,'gym/edit_personal_training_package.html',{'form': form, 'package': package})

class DeletePersonalTrainingPackageView(OwnerRequiredMixin, View):

    def get(self, request, package_id):

        package = get_object_or_404(PersonalTrainingPackage,id=package_id)

        return render(request,'gym/delete_personal_training_package.html',{'package': package})

    def post(self, request, package_id):

        package = get_object_or_404(PersonalTrainingPackage,id=package_id)

        package.delete()

        return redirect('personal_training_package_list')