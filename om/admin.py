from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import OmData
import pandas as pd
from django.utils.translation import gettext_lazy as _

