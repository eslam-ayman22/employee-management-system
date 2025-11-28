from rest_framework import routers
from django.urls import path, include
from .views import (
    CompanyViewSet, DepartmentViewSet, EmployeeViewSet, UserAccountViewSet,
    RoleViewSet, PermissionViewSet, RolePermissionViewSet, UserRoleViewSet,
    EmployeeAddressViewSet, EmployeeDocumentViewSet, OnboardingTaskViewSet, AuditLogViewSet
)

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'users', UserAccountViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'role-permissions', RolePermissionViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'employee-addresses', EmployeeAddressViewSet)
router.register(r'employee-documents', EmployeeDocumentViewSet)
router.register(r'onboarding-tasks', OnboardingTaskViewSet)
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
