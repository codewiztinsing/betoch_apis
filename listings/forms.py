from django import forms
from .models import Listing
# from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget
class ListingForm(forms.ModelForm):
	description = forms.CharField(label='Description',
                   widget=forms.Textarea(attrs={'class': 'form-control'}))
	class Meta:
		model  = Listing
		fields =  (
			'realtor',
			'title',
			'address',
			'city',
			'price',
			'sale_type',
			'bed_rooms',
			'bath_rooms',
			'sqrt',
			'home_type',
			'image',
			'image_1',
			'image_2',
			'image_3',
			'image_4',
			'image_5',

			)