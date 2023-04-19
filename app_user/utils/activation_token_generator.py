from django.contrib.auth.tokens import PasswordResetTokenGenerator
from app_user.models import CustomUser

class ActivateTokenGeneretor(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp: int) -> str:
        return "{}{}{}".format(user.id, timestamp, user.is_active)
    
activation_token_generator = ActivateTokenGeneretor()