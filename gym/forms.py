
from django import forms
from .models import MembershipPlan,TrainingProgram,Equipment,Enquiry,Supplement,PersonalTrainingPackage


class MembershipPlanForm(forms.ModelForm):

    class Meta:

        model = MembershipPlan

        fields = ['plan_name', 'duration', 'price', 'description', 'benefits', 'is_active',]


class TrainingProgramForm(forms.ModelForm):

    class Meta:

        model = TrainingProgram

        fields = ['program_name','description','duration','price','is_active',]


class EquipmentForm(forms.ModelForm):

    class Meta:

        model = Equipment

        fields = ['name','description','price','image','is_available',]



class EnquiryForm(forms.ModelForm):

    class Meta:

        model = Enquiry
        
        fields = ['name', 'phone', 'email', 'item_name', 'message']



class SupplementForm(forms.ModelForm):

    class Meta:

        model = Supplement
        
        fields = ['name','description','price','image','is_available',]


class MembershipEnquiryForm(forms.ModelForm):

    class Meta:
        
        model = Enquiry

        fields = ['name','phone','email','item_name','message',]


class PersonalTrainingPackageForm(forms.ModelForm):

    class Meta:

        model = PersonalTrainingPackage

        fields = ['package_name','description','duration','sessions','price','benefits','is_active',]

        widgets = {'package_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter package name',}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter package description','rows': 3,}),
            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 2 Months',
            }),
            'sessions': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 24',
                'min': 1,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter package price',
                'min': 0,
                'step': '0.01',
            }),
            'benefits': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter benefits, one per line',
                'rows': 4,
            }),
        }
