from django.shortcuts import render
# Create your views hdet
def index(request):
    return render (request,'index.html')
def home(request):
    return render(request, 'home.html')
def list_students(request):
    students={
        "name":"AZOZ",
        "marks":[50,50,50,50],
        "eachsub":{"Software Engineering":0,
                   "Image Processing":0,
                   "Client and Server Programming":0}}
    return render(request, 'show.html', students)
# للتعامل مع for ,if and if else
def edit_students(request):
    students={"total":286,
              "marks":{"Software Engineering":96,
                       "Image Processing":94,
                       "Client and Server Programming":96}}
    return render(request, 'edit.html', students)
def delete_students(request):
    return render(request, 'delete.html')
# التعامل مع الفلاتر التابعة لـ dtl
def index(request):
    name={"fname":"AZOZ"}
    return render(request, 'index.html', name)
def end(request):
    return render (request,'end.html')
def my_view(request):
    # قم بإنشاء متغير (context) لإرساله إلى القالب
    context = {'name': 'World'}
    # استدعاء القالب ومرر له المتغير
    return render(request, 'my_template.html', context)


def student_table(request):
    # البيانات التي تم تقديمها
    students_data = [
        {
            "FirstName" : "أحمد",
            "LastName" : "الهاشمي",
            "Age" : 21,
            "Gender" : "ذكر",
            "Level" : "السنة الثالثة",
            "Status" : "نعم"
        },
        {
            "FirstName" : "محمد",
            "LastName" : "الحضرمي",
            "Age" : 22,
            "Gender" : "ذكر",
            "Level" : "السنة الرابعة",
            "Status" : "نعم"
        },
        {
            "FirstName" : "ليلى",
            "LastName" : "الشريف",
            "Age" : 19,
            "Gender" : "أنثى",
            "Level" : "السنة الأولى",
            "Status" : "نعم"
        },
        {
            "FirstName" : "فهد",
            "LastName" : "القاسمي",
            "Age" : 23,
            "Gender" : "ذكر",
            "Level" : "السنة الخامسة",
            "Status" : "لا"
        },
        {
            "FirstName" : "سارة",
            "LastName" : "الزهري",
            "Age" : 20,
            "Gender" : "أنثى",
            "Level" : "السنة الثانية",
            "Status" : "نعم"
        },
        {
            "FirstName" : "عبدالله",
            "LastName" : "النعيمي",
            "Age" : 24,
            "Gender" : "ذكر",
            "Level" : "السنة الخامسة",
            "Status" : "لا"
        },
        {
            "FirstName" : "مريم",
            "LastName" : "العسيري",
            "Age" : 18,
            "Gender" : "أنثى",
            "Level" : "السنة الأولى",
            "Status" : "نعم"
        },
        {
            "FirstName" : "خالد",
            "LastName" : "المري",
            "Age" : 22,
            "Gender" : "ذكر",
            "Level" : "السنة الرابعة",
            "Status" : "نعم"
        },
        {
            "FirstName" : "هدى",
            "LastName" : "القرشي",
            "Age" : 21,
            "Gender" : "أنثى",
            "Level" : "السنة الثالثة",
            "Status" : "نعم"
        },
        {
            "FirstName" : "بدر",
            "LastName" : "التميمي",
            "Age" : 23,
            "Gender" : "ذكر",
            "Level" : "السنة الخامسة",
            "Status" : "لا"
        }
    ]
    # إرسال البيانات إلى القالب
    return render(request, 'show_students.html', {'students': students_data})