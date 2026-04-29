# projects/forms.py

import re
import time
from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # حقل مخفي ضد البوتات
    # الزائر الحقيقي لا يراه، لكن البوت غالباً يملؤه
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "style": "display:none !important;",
            "tabindex": "-1",
            "autocomplete": "off",
        })
    )

    # وقت فتح الفورم
    # نستعمله باش نعرف واش الرسالة تسيفطات بسرعة غير طبيعية
    started_at = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full Name",
                "autocomplete": "name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email",
                "autocomplete": "email",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write your message here...",
                "rows": 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # عندما يفتح الزائر الصفحة، نضع وقت البداية
        if not self.is_bound:
            self.fields["started_at"].initial = int(time.time())

    def clean_website(self):
        website = self.cleaned_data.get("website")

        if website:
            raise ValidationError("Spam detected.")

        return website

    def clean_started_at(self):
        started_at = self.cleaned_data.get("started_at")

        if not started_at:
            raise ValidationError("Invalid form.")

        now = int(time.time())

        # إذا تسيفط الفورم في أقل من 4 ثواني غالباً بوت
        if now - int(started_at) < 4:
            raise ValidationError("Please wait a few seconds before sending.")

        return started_at

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()

        if len(name) < 2:
            raise ValidationError("Name is too short.")

        # منع أسماء عشوائية فيها نفس الحرف بزاف
        if re.search(r"(.)\1{5,}", name):
            raise ValidationError("Invalid name.")

        return name

    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()

        if len(message) < 20:
            raise ValidationError("Message is too short.")

        # منع أكثر من رابط
        links = re.findall(r"https?://|www\.", message.lower())
        if len(links) >= 2:
            raise ValidationError("Too many links are not allowed.")

        # منع تكرار نفس الحرف أو الرمز بزاف
        if re.search(r"(.)\1{7,}", message):
            raise ValidationError("Message looks like spam.")

        # خاص الرسالة تكون فيها حروف حقيقية
        letters = re.findall(r"[a-zA-ZÀ-ÿ\u0600-\u06FF]", message)
        if len(letters) < 10:
            raise ValidationError("Message is not valid.")

        spam_words = [
            "casino",
            "crypto",
            "bitcoin",
            "loan",
            "viagra",
            "forex",
            "betting",
            "porn",
            "backlink",
            "backlinks",
            "seo backlink",
            "investment",
            "telegram",
        ]

        lower_message = message.lower()

        for word in spam_words:
            if word in lower_message:
                raise ValidationError("Spam message detected.")

        return message