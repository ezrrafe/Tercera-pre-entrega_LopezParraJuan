from django.db import models



class Product(models.Model):

    initial_date = models.DateField()
    deadline = models.DateField()
    customer = models.CharField(max_length = 20)
    part_number = models.CharField(max_length = 30)
    part_description = models.CharField(max_length = 60)
    platform = models.CharField(max_length = 20)
    annual_volume = models.IntegerField()
    lifetime_years = models.IntegerField()

    def __str__(self):

        return f'{self.part_number} - {self.part_description} --- volumen: {self.annual_volume} --- lifetime {self.lifetime_years}'




class Process(models.Model):

    process_type = models.CharField(max_length = 20)
    equipment = models.CharField(max_length = 20)
    pcs_stroke = models.IntegerField()
    lots_per_year = models.IntegerField()

    def __str__(self):

        return f'Operation {self.process_type} --- equipment {self.equipment} --- stroke{self.pcs_stroke}'




class Dimension(models.Model):

    type_material = models.CharField(max_length = 20)
    thickness = models.DecimalField(max_digits=4, decimal_places=2)
    thick_tolerance_min = models.DecimalField(max_digits=2, decimal_places=2)
    thick_tolerance_max = models.DecimalField(max_digits=2, decimal_places=2)
    width = models.DecimalField(max_digits=7, decimal_places=4)
    width_tolerance_min = models.DecimalField(max_digits=2, decimal_places=2)
    width_tolerance_max = models.DecimalField(max_digits=2, decimal_places=2)
    feed = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):

        return f'Material {self.type_material} --- thickness {self.thickness} - width {self.width}'




class Tooling(models.Model):

    type_of_tooling = models.CharField(max_length = 20)
    tooling_cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):

        return f'Tooling {self.type_of_tooling} --- Cost {self.tooling_cost}'
