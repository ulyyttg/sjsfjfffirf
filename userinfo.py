from django.shortcuts import render
import json
import pymysql
from django.http import HttpResponse
from . import util
from authlib.jose import jwt
import time

def userInfo(request):
	try:
		claim = jwt.decode(request.headers['Authorization'],'kexin')
		# print(claim)
		username = claim['username']
		if claim['exp'] < int(time.time()):
			return packApiData(40302, 'Token is expired', '令牌已过期，请重新登录')
	except:
		return util.packApiData(403,'default','请先登录',{})
	return util.packApiData(200,'ok','ok',{"username":username})