from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    # 인증이 되어야만, 목록 조회/포스팅 등록을 허용
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # ('GET', 'HEAD', 'OPTIONS') 인 경우 true
            return True
        
        if (request.method == 'DELETE'):
            return request.user.is_superuser # 또는 request.user.is_staff
        
        return obj.author == request.user