#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from aggregate import (
	calculate_date
)
import csv
from models import (
	ExchangeDetail,
	kessai
)
import datetime


def calc(date):
	a = datetime.datetime.strptime(date, "%Y/%m/%d %H:%M")
	datas = calculate_date(a.strftime("%Y/%m/%d") + " 00:00:00")
	confirm_profit = 0
	for data in datas:
		confirm_profit += data[10]
	return confirm_profit


def input_form(request):
	num = request.GET.get('num', 0)
	tmp = []
	if num is not None:
		for x in xrange(1, int(num) + 1):
			tmp.append(str(x))
	data = {"a": tmp, "num": num}
	return render(request,'polls/input.html', data)


def export_csv(request):
	num = request.POST.get('num')
	person = []
	for x in xrange(1, int(num) + 1):
		tmp_start = request.GET.get("start" + str(x))
		tmp_fin = request.GET.get("fin" + str(x))
		tmp_sikin = request.GET.get("sikin" + str(x))
		tmp_condition = request.GET.get("condition" + str(x))
		tmp_unnyou = request.GET.get("unnyou" + str(x))
		tmp = {
			"id": x,
			"start": tmp_start,
			"fin": tmp_fin,
			"sikin": tmp_sikin,
			"condition": tmp_condition,
			"unnyou": tmp_unnyou
		}
		person.append(tmp)
	flag = request.POST.get('flag')
	if flag == "1":
		try:
			hirose = request.FILES['hirose']
			# TODO hiroseの処理
		except:
			pass
		sbi = request.FILES['sbi']
		# sbiの処理
		sbi_data = csv.reader(sbi)
		for i, data in enumerate(sbi_data):
			if i == 0:
				continue
			if data[9] == '':
				data[9] = 0
			p = kessai(
					order_id=long(data[0]),
					contract_date=datetime.datetime.strptime(data[1], "%Y/%m/%d %H:%M"),
					kendama_num=data[2],
					currency_pair=unicode(data[3].decode('shift-jis')),
					trade_method=unicode(data[4].decode('shift-jis')),
					amount=int(data[5]),
					settlement_price=float(data[6]),
					tatal_sw=int(data[8]),
					realized_profit=int(data[9]),
					total_loss=int(data[10])
			)
			p.save()
		for i, data in enumerate(sbi_data):
			print calc(data[1])
	data = {"persons": person, "num": num}
	return render(request,'polls/export.html', data)
