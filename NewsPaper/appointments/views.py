from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from django.template.loader import render_to_string
from .models import Appointment
