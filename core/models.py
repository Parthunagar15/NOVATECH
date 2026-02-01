from django.db import models


class ContactMessage(models.Model):
    """Stores contact form submissions in SQLite via Django ORM."""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.name} — {self.subject}"
