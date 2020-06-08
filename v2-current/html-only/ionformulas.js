numstring="r0123456789"
function completeformula(x){
	thestring=x
	theformula=""
	addon=""
	if(thestring.charAt(thestring.length-2)=="-" || thestring.charAt(thestring.length-2)=="+"){
			addon="<sup><b>"
			for(j=thestring.length-1;j>thestring.length-3;j--)addon+=thestring.charAt(j);
			addon+="</b></sup>"
			stopat=thestring.length-2
	}
	else stopat=thestring.length;
	for(var j=0;j<stopat;j++){
	if(numstring.indexOf(thestring.charAt(j))>0)theformula+="<sub>"+thestring.charAt(j)+"</sub>";
	else{
		if(thestring.charAt(j)=="-" || thestring.charAt(j)=="+")theformula+="<sup><b>"+thestring.charAt(j)+"</b></sup>";
		else theformula+=thestring.charAt(j);	
	}}
	theformula+=addon
	return(theformula)
}
	
