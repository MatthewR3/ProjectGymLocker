from django import forms



class AddStudentForm(forms.Form):
	student_id = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	yis = forms.CharField(max_length=50)
	teacher = forms.CharField(max_length=50, required=False)
	period = forms.CharField(max_length=50, required=False)
	gender = forms.CharField(max_length=50, required=False)
	locker_number = forms.CharField(max_length=50, required=False)
	note = forms.CharField(max_length=50, required=False)

	def __init__(self, *args, **kwargs):
	    super(AddStudentForm, self).__init__(*args, **kwargs)
	    self.fields['teacher'].widget.attrs['placeholder'] = 'Optional'
	    self.fields['period'].widget.attrs['placeholder'] = 'Optional'
	    self.fields['gender'].widget.attrs['placeholder'] = 'Optional'
	    self.fields['locker_number'].widget.attrs['placeholder'] = 'Optional'
	    self.fields['note'].widget.attrs['placeholder'] = 'Optional'



class AddLockForm(forms.Form):
	serial = forms.CharField(max_length=50)
	combination = forms.CharField(max_length=50)
	owner = forms.CharField(max_length=50, required=False)

	def __init__(self, *args, **kwargs):
	    super(AddLockForm, self).__init__(*args, **kwargs)
	    self.fields['owner'].widget.attrs['placeholder'] = 'Optional'



# This form is no longer used for the class view prompt function. Instead, an AJAX call is used.
'''
class TeacherSelect(forms.Form):

	from GymLocker import services

	TEACHER_CHOICES = services.get_teacher_names()

	teacher_name = forms.ChoiceField(choices=TEACHER_CHOICES)

	def __init__(self, *args, **kwargs):
	    super(TeacherSelect, self).__init__(*args, **kwargs)
	    self.fields['teacher_name'].widget.attrs['id'] = 'searchbar'
'''