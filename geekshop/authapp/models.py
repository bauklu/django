from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from geekshop.settings import ACTIVATION_KEY_TTL, DOMAIN_NAME, EMAIL_HOST_USER


def calc_activation_key_expires():
    return now() + timedelta(hours=ACTIVATION_KEY_TTL)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст', null=True)
    avatar = models.ImageField('аватар', upload_to='avatars', blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=calc_activation_key_expires)

    def basket_total_cost(self):
        return sum(map(lambda x: x.product_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.quantity, self.basket.all()))

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
        return 1, {}

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires
        # return now() - self.date_joined > timedelta(hours=ACTIVATION_KEY_TTL)

    def send_verify_mail(self):
        verify_link = reverse('auth:verify',
                              kwargs={'email': self.email,
                                      'activation_key': self.activation_key})

        subject = f'Подтверждение учетной записи {self.username}'
        message = f'Для подтверждения учетной записи {self.username} на портале ' \
                  f'{DOMAIN_NAME} перейдите по ссылке: \n{DOMAIN_NAME}{verify_link}'

        return send_mail(subject, message, EMAIL_HOST_USER, [self.email], fail_silently=False)


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
    )

    user = models.OneToOneField(ShopUser, primary_key=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)
