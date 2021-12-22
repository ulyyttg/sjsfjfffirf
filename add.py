from django.shortcuts import render
import json
import pymysql
from django.http import HttpResponse
from . import util
from authlib.jose import jwt
import time


def add(request):
	try:
		claim = jwt.decode(request.headers['Authorization'],'kexin')
		# print(claim)
		username = claim['username']
		if claim['exp'] < int(time.time()):
			return packApiData(40302, 'Token is expired', '令牌已过期，请重新登录')
		creator_id = claim['userid']
	except:
		return util.packApiData(403,'default','请先登录',{})	
	name = request.POST.get('name')
	date = str(request.POST.get('date'))
	phone = request.POST.get('phone')
	content = request.POST.get('content')
	address = request.POST.get('address')
	time_stamp = date
	repairman = '测试维修师'
	status = 1
	pid = util.makeRandomStr(5)
	if name and phone and content and address and date:
		print(name,phone,content,address,date)
		connection = pymysql.connect(host ='159.75.47.53',port = 3306,user = "root",passwd = "124536")
		cursor = connection.cursor()
		sql = "INSERT INTO data.record (name,address,creator_id,time_stamp,phone,content,repairman,status,pid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(sql,[name,address,creator_id,time_stamp,phone,content,repairman,status,pid])
		connection.commit()
	else:
		return util.packApiData(401,'lack of param','缺少参数',{})
	return util.packApiData(200,'ok','ok',{})