from django.shortcuts import render
import urllib2
from django.http import HttpResponse,HttpResponseRedirect
# lists = [ 9129911, 9129199, 9127761, 9128141, 9128264, 9127792, 9129248, 9127092, 9128367]
# Create your views here.
import json
import ast
from django.views.decorators.csrf import csrf_exempt
import datetime


responce = {}


def top_news(request):
	req = urllib2.Request('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
	tp_ten = urllib2.urlopen(req).read()
	llist = ast.literal_eval(tp_ten)[:10]
	j = 0
	reponce = {}
	for i in llist:
		req = urllib2.Request('https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty' %i)
		Hn_data = urllib2.urlopen(req).read()
		reponce[j] = json.loads(Hn_data)
		# reponce[j] = {"id": data["id"],"title":data["title"],"by":data["by"],"score":data["score"],"url"}
		j += 1
	# print reponce
	return render(request,'top_ten.html',{"res":reponce})



@csrf_exempt
def new_discr(request):
	nws_id = request.GET['qry']
	req = urllib2.Request('https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty' %nws_id)
	Hn_data = urllib2.urlopen(req).read()
	data = json.loads(Hn_data)
	data["time"] = datetime.datetime.fromtimestamp(int(data["time"])).strftime('%Y-%m-%d %H:%M:%S')
	return render(request,'discription.html',{"disc":data})