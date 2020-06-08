function number(x,y,z){
if(x==0)return "0.00";
else{
x<0?sign="-":sign="";
x=Math.abs(x)
sfigs=Math.floor(y)
if(sfigs<1)sfigs=1;
base=Math.pow(10,sfigs)
count=0
if(x<base/10){
	while(x<base/10){x=x*10;count--};
	}
else{
	if(x>base){
		while(x>base){x=x/10;count++};
		}
	}
if(x==base){x=Math.round(base/10);count++};
x=Math.round(x)+""
coeff=x.substring(0,1)+"."+x.substring(1,sfigs+1)
enumber=coeff+"e"+(count+sfigs-1)
dnumber=decnot(coeff,sfigs,count)
snumber=scinot(enumber)
if(z==1)return sign+enumber
if(z==2)return sign+snumber
if(z==3)return sign+dnumber
}}
function scinot(x){
	howlong=x.length
	split=x.indexOf("e")
	coeff=x.substring(0,split)
	snumber=coeff+"*10<sup>"+x.substring(split+1,howlong)+"</sup>"
	return snumber
	}
function decnot(x,sfigs,count){
	dnumber=x
	for(j=1;j<sfigs;j++)dnumber=dnumber*10;
	dnumber=Math.round(dnumber)
	howlong=sfigs
	exp=count+sfigs-1
	if(exp<0){
		intro="0."
		zeros=Math.abs(exp)-1
		for(j=1;j<=zeros;j++)intro+="0";
		dnumber=intro+dnumber
	}
	else{
		dnumber=""+dnumber
		diff=howlong-exp-1
	 	if(diff<0)for(h=diff;h<0;h++)dnumber+="0";
		if(diff>0)dnumber=dnumber.substring(0,exp+1)+"."+dnumber.substring(exp+1,howlong);
	}
	return dnumber
}

		
	
	
	
