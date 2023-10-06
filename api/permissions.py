from rest_framework.permissions import BasePermission

class CustomUserPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class CustomUserDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        
class ProjectPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class ProjectDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        
class TaskPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class TaskDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff