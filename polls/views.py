from django.shortcuts import render
import pandas as pd
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def index1(request):
	return render(request,'polls/index1.html')

def index2(request):
	return render(request,'polls/index2.html')

def index3(request):
	# csvfile = request.GET["csvname1"]
	# csvfile = "test.csv"
	a = pd.read_csv("test.csv")
	print a
	return render(request,'polls/index3.html')

def index4(request):
	return render(request,'polls/index4.html')



