from django.shortcuts import render
import json
import pymysql
from django.http import HttpResponse
from . import util
from authlib.jose import jwt
import time

def userData(username,password):
	connection = pymysql.connect(host ='159.75.47.53',port = 3306,user = "root",passwd = "124536")
	sql = 'SELECT password,userid,role,name FROM data.user WHERE username = %s'
	cursor = connection.cursor()
	cursor.execute(sql,[username])
	result = cursor.fetchone()
	try:
		if password == result[0]:
			userid = result[1]
			role = result[2]
			name = result[3]
			return userid,role,name
		else:
			return 0,0,0
	except:
		return 0,0,0
	# userid
	# 0 登录失败
	# 1 user
	# 2 admin