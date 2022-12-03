
var dico=["BONJOUR","AVOIR","AVION","ANACONDA", "ANTICONSTITUTIONNELLEMENT", "FEYZIN", "SUPERPLAYART", "SFR", "FREE", "CHROMEBOOK", "TOTAL", "REEF"];
	var solution=[]; 
	var essai=[];
	var nombreErreurs=0;
    var mot;
	function initialise()
	{
		var chaine="";
		for(i=0;i<26;i++)
		{
			lettre=String.fromCharCode(65+i);
			chaine+="<input type='button' class='myButton' value='"+lettre+"' onclick='clique("+'"'+lettre+'"'+");'>";
		}
		
		document.getElementById("boutons").innerHTML=chaine;
		
		commence();
	}

	function commence()
	{
		document.getElementById("pendu").src="./img/"+0+".png";
		nombreErreurs=0;
		document.getElementById("essai").innerHTML=nombreErreurs;
		essai=[];
		solution=[];
		var motATrouver=tireUnMot();
        mot = motATrouver
        
		for(i=0;i<motATrouver.length;i++)
		{
			solution[i]=motATrouver.substring(i,i+1);
			essai[i]="?";
		}
		afficheMot();
	}
	
	function afficheMot()
	{
		chaine="<table><tr>";
		for(i=0;i<essai.length;i++)
		{
			chaine+="<td><h1>"+essai[i]+"</h1></td>";
		}
		chaine+="</tr></table>";
		document.getElementById("lescases").innerHTML=chaine;
	}
	
	function tireUnMot()
	{
		alea=Math.floor(Math.random() * dico.length);
		return dico[alea];
	}	
	
	function clique(lettreChoisie)
	{
		
		present=false;
		for(i=0;i<solution.length;i++)
		{
			if(solution[i] == lettreChoisie)
			{
				essai[i]=lettreChoisie;
				present=true;
			}
		}
		afficheMot();
		if(present)
		{
			//on teste si on a gagné
			gagne=true;
			for(i=0;i<essai.length;i++)
			{
				if(essai[i]=="?")
				{
					gagne=false;
					break;
				}
			}
			if(gagne)
			{
                document.getElementById('historique').innerHTML+="<essai2>"+mot+" : "+nombreErreurs+"</essai2>"+"<br>";
				commence();
			}
		}
		else
		{   
			nombreErreurs++;
            document.getElementById("essai").innerHTML=nombreErreurs;
            if (nombreErreurs < 11){
                document.getElementById("pendu").src="./img/"+nombreErreurs+".png"
            }else{
                document.getElementById("pendu").src="./img/"+11+".png"
                document.getElementById('historique').innerHTML+="<essai>"+mot+" : "+nombreErreurs+"</essai>"+"<br>";
				commence();
            }
            
		}
    }



