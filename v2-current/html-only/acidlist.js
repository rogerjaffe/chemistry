thenumbers="0123456789"
//0=neutrals,3=weakacids,4=weakbases,2=strong base
thelist=new Array()
thelist[0]=new Array("Cl",0)
thelist[1]=new Array("NO3",0)
thelist[2]=new Array("I",0)
thelist[3]=new Array("Br",0)
thelist[4]=new Array("ClO4",0)
thelist[5]=new Array("C2H3O2",3,1.8,5)
thelist[6]=new Array("NH3",4,1.8,5)
thelist[7]=new Array("C5H5N",4,1.5,9)
thelist[8]=new Array("C3H3O2",3,5.5,5)
thelist[9]=new Array("C7H5O2",3,6.3,5)
thelist[10]=new Array("C2H2BrO2",3,1.3,3)
thelist[11]=new Array("C4H7O2",3,1.5,5)
thelist[12]=new Array("C2H2ClO2",3,1.4,3)
thelist[13]=new Array("ClO2",3,1.1,2)
thelist[14]=new Array("OCN",3,3.5,4)
thelist[15]=new Array("C2HCl2O2",3,5.5,2)
thelist[16]=new Array("C2H2FO2",3,2.6,3)
thelist[17]=new Array("CHO2",3,1.8,4)
thelist[18]=new Array("N3",3,1.9,5)
thelist[20]=new Array("CN",3,6.2,10)
thelist[21]=new Array("F",3,6.6,4)
thelist[22]=new Array("OBr",3,2.5,9)
thelist[23]=new Array("OCl",3,2.9,8)
thelist[24]=new Array("IO3",3,1.6,1)
thelist[25]=new Array("NO2",3,7.2,4)
thelist[26]=new Array("C3H5O2",3,1.3,5)
thelist[27]=new Array("C5H6NH2",4,7.4,10)
thelist[28]=new Array("C2H5NH2",4,4.3,4)
thelist[29]=new Array("C9H7N",4,2.5,9)
thelist[30]=new Array("CH3NH2",4,4.2,4)
thelist[31]=new Array("C5H11N",4,1.3,3)
thelist[32]=new Array("C5H5N",4,1.5,9)
thelist[33]=new Array("C9H7N",4,6.3,10)
thelist[34]=new Array("C6H15O3N",4,5.8,7)
thelist[35]=new Array("(C2H5)3N",4,5.2,4)
thelist[35]=new Array("(CH3)3N",4,6.3,5)
thelist[19]=new Array("OH",2)
key=0
anskey=""
function makeformula(x){
	theformula=""
	for(j=0;j<thelist[x][0].length;j++){
		thenumbers.indexOf(thelist[x][0].charAt(j))>0?theformula+=("<sub>"+thelist[x][0].charAt(j)+"</sub>"):theformula+=thelist[x][0].charAt(j)
	}
	if(thelist[x][1]==0){
		option=Math.floor(3*Math.random())
		if(option==0){theformula="H"+theformula;key=0};
		if(option==1){theformula="K"+theformula;key=2};
		if(option==2){theformula+="<sup>-</sup>";key=2}
	}
	if(thelist[x][1]==2){
		if(Math.random()>.5)theformula="K"+thelist[x][0];
		else theformula="Na"+thelist[x][0]
		key=1
	}
	if(thelist[x][1]==3){
		option=Math.floor(3*Math.random())
		if(option==0){theformula="H"+theformula;key=3;coef=thelist[x][2]}
		if(option==1){theformula="Na"+theformula;key=4;coef=10/thelist[x][2]}
		if(option==2){theformula+="<sup>-</sup>";key=4;coef=10/thelist[x][2]}	
	}
	if(thelist[x][1]==4){
		option=Math.floor(2*Math.random())
		if(option==0){theformula=theformula;key=4;coef=thelist[x][2]}
		if(option==1){
			theformula=adjust(x)	
			theformula+="<sup>+</sup>"
			key=3
			coef=10/thelist[x][2]
		}	
	}
	anskey=""+thelist[x][1]+key
	return theformula
}
function adjust(x){
	lastspot=thelist[x][0].charAt(thelist[x][0].length-1)
	if(thenumbers.indexOf(lastspot)>0){
		theformula=""
		for(j=0;j<thelist[x][0].length-1;j++){
		thenumbers.indexOf(thelist[x][0].charAt(j))>0?theformula+=("<sub>"+thelist[x][0].charAt(j)+"</sub>"):theformula+=thelist[x][0].charAt(j)
	}
	theformula+="<sub>"+(1*lastspot+1)+"</sub>"
	}
	else theformula+="H";
	return theformula
}

		





