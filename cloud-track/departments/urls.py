from django.urls import path
from django.contrib.auth.decorators import login_required
from departments.views import DepartmentView, DepartmentListView, DepartmentCreateView

urlpatterns = [
    # path('', DepartmentView.as_view(), name='departments' ),
    path('index', DepartmentListView.as_view(), name='departments.index'),
    path('create', login_required(DepartmentCreateView.as_view()), name='departments.create'),
    path('<int:pk>', DepartmentView.as_view(), name='department'),

]
