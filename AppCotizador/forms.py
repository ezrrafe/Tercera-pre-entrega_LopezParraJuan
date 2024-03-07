from django import forms


class ProductFormulario(forms.Form):

    initial_date = forms.DateField()
    deadline = forms.DateField()
    customer = forms.CharField(max_length = 20)
    part_number = forms.CharField(max_length = 30)
    part_description = forms.CharField(max_length = 60)
    platform = forms.CharField(max_length = 20)
    annual_volume = forms.IntegerField()
    lifetime_years = forms.IntegerField()




class ProcessFormulario(forms.Form):

    process_type = forms.CharField(max_length = 20)
    equipment = forms.CharField(max_length = 20)
    pcs_stroke = forms.IntegerField()
    lots_per_year = forms.IntegerField()




class DimensionFormulario(forms.Form):

    type_material = forms.CharField(max_length = 20)
    thickness = forms.DecimalField(max_digits=4, decimal_places=2)
    thick_tolerance_min = forms.DecimalField(max_digits=2, decimal_places=2)
    thick_tolerance_max = forms.DecimalField(max_digits=2, decimal_places=2)
    width = forms.DecimalField(max_digits=7, decimal_places=4)
    width_tolerance_min = forms.DecimalField(max_digits=2, decimal_places=2)
    width_tolerance_max = forms.DecimalField(max_digits=2, decimal_places=2)
    feed = forms.DecimalField(max_digits=7, decimal_places=4)




class ToolingFormulario(forms.Form):

    type_of_tooling = forms.CharField(max_length = 20)
    tooling_cost = forms.DecimalField(max_digits=8, decimal_places=2)
