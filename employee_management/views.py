from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Education, Office

def add_employee(request):
    if request.method == "POST":
        employee = Employee.objects.create(
            name=request.POST.get("name"),
            date_of_birth=request.POST.get("date_of_birth"),
            address=request.POST.get("address"),
            position=request.POST.get("position"),
            sex=request.POST.get("sex"),
            age=request.POST.get("age"),
        )
        Education.objects.create(
            employee=employee,
            collegename=request.POST.get("collegename"),
            address=request.POST.get("college_address"),
            degreecompleted=request.POST.get("degreecompleted"),
            major=request.POST.get("major"),
            gpa=request.POST.get("gpa"),
            year=request.POST.get("graduation_year"),
        )
        Office.objects.create(
            employee=employee,
            officeName=request.POST.get("officeName"),
            address=request.POST.get("office_address"),
            year=request.POST.get("office_year"),
            totalEmployee=request.POST.get("totalEmployee"),
            establishedYear=request.POST.get("establishedYear"),
            netWorth=request.POST.get("netWorth"),
        )
        return redirect('edit_employee')
    return render(request, "add_employee.html")


def edit_employee(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "delete":
            employee_id = request.POST.get("delete_id")
            employee = get_object_or_404(Employee, id=employee_id)
            employee.delete()
            return redirect('edit_employee')  

        elif action == "edit":
            employee_id = request.POST.get("edit_id")
            employee = get_object_or_404(Employee, id=employee_id)
            education = Education.objects.filter(employee=employee).first()
            office = Office.objects.filter(employee=employee).first()
            return render(request, "edit_employee.html", {
                "edit_employee": employee,
                "edit_education": education,
                "edit_office": office,
                "combined_data": get_combined_data(),
            })

        elif action == "save":
            employee_id = request.POST.get("employee_id")
            employee = get_object_or_404(Employee, id=employee_id)
            employee.name = request.POST.get("name")
            employee.date_of_birth = request.POST.get("date_of_birth")
            employee.address = request.POST.get("address")
            employee.position = request.POST.get("position")
            employee.sex = request.POST.get("sex")
            employee.age = request.POST.get("age")
            employee.save()

            education = Education.objects.filter(employee=employee).first()
            if education:
                education.collegename = request.POST.get("collegename")
                education.address = request.POST.get("college_address")
                education.degreecompleted = request.POST.get("degreecompleted")
                education.major = request.POST.get("major")
                education.gpa = request.POST.get("gpa")
                education.year = request.POST.get("graduation_year")
                education.save()

            office = Office.objects.filter(employee=employee).first()
            if office:
                office.officeName = request.POST.get("officeName")
                office.address = request.POST.get("office_address")
                office.year = request.POST.get("office_year")
                office.totalEmployee = request.POST.get("totalEmployee")
                office.establishedYear = request.POST.get("establishedYear")
                office.netWorth = request.POST.get("netWorth")
                office.save()

            return redirect('edit_employee')  

    return render(request, "edit_employee.html", {
        "combined_data": get_combined_data(),
    })


def get_combined_data():
    """
    Fetch all employees and their related Education and Office data.
    """
    combined_data = []
    employees = Employee.objects.all()
    for employee in employees:
        education = Education.objects.filter(employee=employee).first()
        office = Office.objects.filter(employee=employee).first()
        combined_data.append({
            "employee": employee,
            "education": education,
            "office": office,
        })
    return combined_data


from django.shortcuts import render
from .models import Employee, Education, Office

from django.shortcuts import render
from .models import Employee, Education, Office

def filter_employees(request):
    # Fetch unique values for dropdowns
    positions = Employee.objects.values_list("position", flat=True).distinct()
    degrees = Education.objects.values_list("degreecompleted", flat=True).distinct()
    majors = Education.objects.values_list("major", flat=True).distinct()
    gpas = Education.objects.values_list("gpa", flat=True).distinct().order_by("gpa")

    # Collect filter criteria from the request
    filters = {
        "sex": request.GET.get("sex"),
        "position": request.GET.get("position"),
        "degree": request.GET.get("degree"),
        "major": request.GET.get("major"),
        "gpa": request.GET.get("gpa"),
    }

    # Start with all employees and apply filters conditionally
    employees = Employee.objects.all()

    if filters["sex"]:
        employees = employees.filter(sex=filters["sex"])
    if filters["position"]:
        employees = employees.filter(position=filters["position"])
    if filters["degree"]:
        employees = employees.filter(education__degreecompleted=filters["degree"])
    if filters["major"]:
        employees = employees.filter(education__major=filters["major"])
    if filters["gpa"]:
        employees = employees.filter(education__gpa__gte=filters["gpa"])

    # Combine data for rendering in the table
    combined_data = []
    for employee in employees:
        education = Education.objects.filter(employee=employee).first()
        office = Office.objects.filter(employee=employee).first()
        combined_data.append({
            "employee": employee,
            "education": education,
            "office": office,
        })

    return render(request, "filter_employees.html", {
        "combined_data": combined_data,
        "filters": filters,
        "positions": positions,
        "degrees": degrees,
        "majors": majors,
        "gpas": gpas,
    })
