import time
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  testapp.forms import SignUpForm,Irrigation
from testapp import forms
import requests as r
from testapp.models import cropdetail,irrigation,Userphone
import datetime
from testapp.forms import DateForm,CropType
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy



#home page conatineg current field condition
@login_required
def home_page(request):
	if(request.user.is_authenticated):
		username= request.user.username
	k=Userphone.objects.get(username1=username)
	print(k)
	print(k.phoneno)
	#r.post('https://api.thingspeak.com/update?api_key=DQANZY33TBG1Z8UY&field1='+str(k.phoneno))
	#hold data of current filed
	api='http://api.openweathermap.org/data/2.5/weather?appid=b20d784cf83f0102efcc1d90dbe3e84d&q=Raipur'
	json_data=r.get(api).json()
	b=json_data['wind']['speed']
	return render(request,'testapp/home.html',{'b':b,'username':username})

#weather foarcast page hold data about 4 days weather forcast	
@login_required
def weatherforcast(request):
	count=0
	sum=0
	sum1=0
	call=0
	a=[]
	api='http://api.openweathermap.org/data/2.5/forecast?APPID=b20d784cf83f0102efcc1d90dbe3e84d&q='
	url=api+'raipur'
	json_data=r.get(url).json()
	for i in range(32):
	    clouds=json_data['list'][i]['weather'][0]['main']
	    count=count+1
	    hum=json_data['list'][i]['main']['humidity']
	    sum1=sum1+hum
	    if(clouds=='Rain'):
	        k=json_data['list'][i]['rain']['3h']
	        sum=sum+k
	    if(count%8==0):
	    	k=datetime.date.today() + datetime.timedelta(days=count/8)
	    	hum=sum1/8
	    	sum1=0
	    	temp=json_data['list'][i]['main']['temp']
	    	print(temp)
	    	c=[]
	    	c.append(k)
	    	c.append(int(hum))
	    	c.append(int(temp-273))
	    	c.append(int(sum))
	    	a.append(c)
	    	c=[]
	    	sum=0
	return render(request,'testapp/weather.html',{'a':a})



#motor button and action page	
@login_required
def motor(request):
	res2=r.get('https://api.thingspeak.com/channels/816679/fields/1/last.json?api_key=M518Q0Q08GLDRP42&results=2')
	val1=res2.json()
	k=val1['field1']
	print(k)
	return render(request,'testapp/motor.html',{'k':k})
def stop(request):
	res2=r.get('https://api.thingspeak.com/channels/816679/fields/1/last.json?api_key=M518Q0Q08GLDRP42&results=2')
	val1=res2.json()
	k=val1['field1']
	if(k=='1'):
		r.post(' https://api.thingspeak.com/update?api_key=SPCJY69R8UC9CBXE&field1=0')
	else:
		r.post(' https://api.thingspeak.com/update?api_key=SPCJY69R8UC9CBXE&field1=1')
	return render(request,'testapp/motor.html')



#logout 
def logout(request):
	return render(request,'testapp/logout.html')
#godown	
#1main page
@login_required
def godown1(request):
	return render(request,'testapp/godown.html')
#2add crop
def signup(request):
	form=SignUpForm()
	if request.method=='POST':
		form=forms.SignUpForm(request.POST)
		if form.is_valid():
			form.save(commit=True) 
		username=None
		if(request.user.is_authenticated()):
			username = request.user.username
			qs=cropdetail.objects.all()
		return render(request,'testapp/detailcrop.html',{'qs':qs,'name1':username})
	return render(request,'testapp/signup.html',{'form':form})
#3showcrop
def godown(request):
	username=None
	if(request.user.is_authenticated):
		username = request.user.username
		qs=cropdetail.objects.all()
	return render(request,'testapp/detailcrop.html',{'qs':qs,'name1':username})
#4deletecrop
class BeerDeleteView(DeleteView):
	model=cropdetail
	success_url=reverse_lazy('home')
#5 updatecrop
class BeerUpdateView(UpdateView):
	model=cropdetail
	fields=('cropquantity',)


#sowing detail logic
@login_required
def croptype(request):
	form=CropType()
	return render(request,'testapp/croptype.html',{'form':form})
def date(request):
	crop=request.GET['TypeOfCrop']
	request.session['TypeOfCrop']=crop
	crop=request.session['TypeOfCrop']
	form=DateForm()
	return render(request,'testapp/date.html',{'form':form,'crop':crop})
def sowing(request):
	date=request.GET['date']
	request.session['date']=date
	k1=request.session['TypeOfCrop']
	k=request.session['date']
	date=k[0:10] 
	r.post('https://api.thingspeak.com/update?api_key=MYLRF7RQSCG2HK6I&field1='+str(k1)+'&field2='+str(date))
	return render(request,'testapp/sowing.html',{'date':date})







#irrigation 	
@login_required
def irrigation1(request):
	form=Irrigation()	
	return render(request,'testapp/irrigate.html',{'form':form})
def detail(request):
	gf=request.GET['CropStage']
	request.session['CropStage']=gf
	k=request.session['CropStage']     #stage of crop inserted by user
	print(type(k))
	res2=r.get('https://api.thingspeak.com/channels/816674/feeds/last.json?api_key=6JIRRMHSVNUTBHKT&results=2')
	val1=res2.json()
	water=0
	moisture=val1['field2']
	if k== '1':
		water=55
	elif k== '2':
		water=225
	elif k== '3':
		water=500
	elif k== '4':
		water=425
	elif k== '5':
		water=120
	else:
		water=0
	water=water-int(moisture)
	api='http://api.openweathermap.org/data/2.5/forecast?APPID=b20d784cf83f0102efcc1d90dbe3e84d&q='
	url=api+'raipur'
	sum=0
	print(water)
	json_data=r.get(url).json()
	for i in range(32):
		clouds=json_data['list'][i]['weather'][0]['main']
		if(clouds=='Rain'):
			k=json_data['list'][i]['rain']['3h']
			sum=sum+k
	print(sum)
	water=water-sum
	print(water)
	if(water<=0):
		p="Thier is no need of water because thier is a chance of rain in your area"
	else:
		water=int(float(water)/25.4)
		print(water)
		rate=int(102789/10000)
		p=float(water*rate)
		p=p/60
		p=p*60
	return render(request,'testapp/detail.html',{'k':p})