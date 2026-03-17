from rest_framework.throttling import UserRateThrottle

class LoginUserThrottle(UserRateThrottle):
    scope = 'user'

    def get_rate(self):
        return '5/min'  # 5 requests per minute per user

    def get_cache_key(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return None  # skip anonymous users
        return f"user-{request.user.pk}"  # count per user