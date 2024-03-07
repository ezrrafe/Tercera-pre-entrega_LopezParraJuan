from django.shortcuts import render
from AppCotizador.models import *
from AppCotizador.forms import *



def inicio(request):

    return render(request, "inicio.html")




def crear_product(request):

    if request.method == "POST":

        formulario = ProductFormulario(request.POST)

        if formulario.is_valid():

            info_dicc = formulario.cleaned_data

        product_nuevo = Product(
            initial_date=info_dicc["initial_date"],
            deadline=info_dicc["deadline"],
            customer=info_dicc["customer"],
            part_number=info_dicc["part_number"],
            part_description=info_dicc["part_description"],
            platform=info_dicc["platform"],
            annual_volume=info_dicc["annual_volume"],
            lifetime_years=info_dicc["lifetime_years"]
            )

        product_nuevo.save()

        return render(request, "inicio.html")

    else:

        formulario = ProductFormulario()

    return render(request, "crear_product.html", {"formu":formulario})




def crear_process(request):

    if request.method == "POST":

        formulario = ProcessFormulario(request.POST)

        if formulario.is_valid():

            info_dicc = formulario.cleaned_data

        process_nuevo = Process(
            process_type=info_dicc["process_type"],
            equipment=info_dicc["equipment"],
            pcs_stroke=info_dicc["pcs_stroke"],
            lots_per_year=info_dicc["lots_per_year"]
            )

        process_nuevo.save()

        return render(request, "inicio.html")

    else:

        formulario = ProcessFormulario()

    return render(request, "crear_process.html", {"formu":formulario})




def crear_dimension(request):

    if request.method == "POST":

        formulario = DimensionFormulario(request.POST)

        if formulario.is_valid():

            info_dicc = formulario.cleaned_data

        dimension_nuevo = Dimension(
            type_material=info_dicc["type_material"],
            thickness=info_dicc["thickness"],
            thick_tolerance_min=info_dicc["thick_tolerance_min"],
            thick_tolerance_max=info_dicc["thick_tolerance_max"],
            width=info_dicc["width"],
            width_tolerance_min=info_dicc["width_tolerance_min"],
            width_tolerance_max=info_dicc["width_tolerance_max"],
            feed=info_dicc["feed"]
            )

        dimension_nuevo.save()

        return render(request, "inicio.html")

    else:

        formulario = DimensionFormulario()

    return render(request, "crear_dimension.html", {"formu":formulario})




def crear_tooling(request):

    if request.method == "POST":

        formulario = ToolingFormulario(request.POST)

        if formulario.is_valid():

            info_dicc = formulario.cleaned_data

        tooling_nuevo = Tooling(
            type_of_tooling=info_dicc["type_of_tooling"],
            tooling_cost=info_dicc["tooling_cost"]
            )

        tooling_nuevo.save()

        return render(request, "inicio.html")

    else:

        formulario = ToolingFormulario()

    return render(request, "crear_tooling.html", {"formu":formulario})




def buscar_product(request):

    if request.method == "GET":

        mensaje = f'Estamos buscando el item {request.GET}'

    else:

        mensaje = f' '

    return render(request, "resultados_product.html", {"mensaje":mensaje})
