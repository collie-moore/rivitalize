from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.


def random_code(size=8, chars=string.ascii_letters):
    return "".join(random.choice(chars) for _ in range(size)).upper()



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class  Package(BaseModel):
    name = models.CharField(max_length=55, null=False, blank=False)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="logos", null=True)
    slug = models.SlugField(null=True, db_index=True, blank=True)

    class Meta:
        verbose_name_plural = "packages"
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Voucher(BaseModel):
    package_name = models.ForeignKey(Package, on_delete=models.DO_NOTHING, related_name="package")
    redeemed_status = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(null=True, db_index=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="created_by")
    redeemed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="redeemed_by")

    class Meta:
        verbose_name_plural = "Vouchers"
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.package_name.name
