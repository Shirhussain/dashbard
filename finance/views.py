from django.shortcuts import render

from .models import Company

def company_article(request):
	return render(request,"finance/article.html",{})