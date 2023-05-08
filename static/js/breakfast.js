btn=document.getElementById('btn');

btn.onclick=()=>{
    marks=document.getElementById('marks').value.trim();
    dish1=document.getElementById('dish1').value.toLowerCase().trim();
    dish2=document.getElementById('dish2').value.toLowerCase().trim();
    dish3=document.getElementById('dish3').value.toLowerCase().trim();
    dish4=document.getElementById('dish4').value.toLowerCase().trim();

    ans1="gohan";
    ans2="miso shiru";
    ans3="natto";
    ans4="tamago kake gohan";


    if(marks=="20" && dish1==ans1 && dish2==ans2 && dish3==ans3 && dish4==ans4){
        window.location.href = "/tvshow";      
    }
    else{

        alert("Your Answers are wrong please try again!!");
    }

}