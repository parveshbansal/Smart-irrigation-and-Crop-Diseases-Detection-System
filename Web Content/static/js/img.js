var x,y,z,p;
var h2=document.getElementById('p');
var h1=document.getElementById('q');
var h=document.getElementById('r');
var k=document.getElementById('a');
var d=document.getElementById('t');
function bansal(){
$.getJSON("https://api.thingspeak.com/channels/816674/feeds/last.json?api_key=6JIRRMHSVNUTBHKT&results=2",function(data){
	x=data['field1']
	//field condion function
	y=data['field2']
	z=data['field3']
			h2.textContent=x;
			h1.textContent=y;
			h.textContent=z;
});
}
function bansal3(){
$.getJSON("https://api.thingspeak.com/channels/814542/feeds/last.json?api_key=GP5ITWB1ARGW7DHV&results=2",function(data){
	x=data['field1']
	//field condion function
	if(x==='1'){
				d.textContent='wheat';
			}
			else if(x==='2'){
				d.textContent='Ground Nuts';
			}
			else if(x==='3'){
				d.textContent='Garden flowers';
			}
			else if(x==='4'){
				d.textContent='Maize';
			}
			else if(x==='5'){
				d.textContent='Paddy';
			}
			else if(x==='6'){
				d.textContent='Potato';
			}
			else if(x==='7'){
				d.textContent='Pulse';
			}else if(x==='8'){
				d.textContent='SugerCane';
			}
			else{

				d.textContent='Coffee'
			}
});
}
//moter javascript
function bansalji(){
$.getJSON("https://api.thingspeak.com/channels/816679/fields/1/last.json?api_key=M518Q0Q08GLDRP42&results=2",function(data){
	p=data['field1']
	if(p==='1'){
		k.textContent='OFF';
	}			
	else{
		k.textContent='ON';
	}
});
}
bansal3();
setInterval(function () {
    bansal();
    bansalji();

}, 500);