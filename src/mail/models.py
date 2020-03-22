from django.contrib.postgres.indexes import GinIndex
from django.db import models


class Mail(models.Model):
    user_from = models.ForeignKey(
        "auth.User",
        null=False,
        related_name="sent_mail",
        verbose_name="From",
        on_delete=models.CASCADE,
    )
    user_to = models.ForeignKey(
        "auth.User",
        null=False,
        related_name="received",
        verbose_name="To",
        on_delete=models.CASCADE,
    )
    subject = models.TextField(
        blank=False,
        null=False,
        verbose_name="Subject",
    )
    text = models.TextField(
        verbose_name="Text"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",

    )
    unread = models.BooleanField(
        default=True,
        verbose_name="Is unread",
    )

    class Meta:
        ordering = ["-pk"]
        indexes = [
            models.Index(fields=['user_from']),
            models.Index(fields=['user_to']),
            models.Index(fields=['created_at']),
            GinIndex(fields=['subject'])
        ]

        verbose_name = "Mail"
        verbose_name_plural = "Mails"
