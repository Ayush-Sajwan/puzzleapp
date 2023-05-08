btn=document.getElementById('btn');

btn.onclick=()=>{
    s1=document.getElementById('s1').value.toLowerCase().trim();
    s2=document.getElementById('s2').value.toLowerCase().trim();
    s3=document.getElementById('s3').value.toLowerCase().trim();
    s4=document.getElementById('s4').value.toLowerCase().trim();

    ans1="14125";
    ans2="tokyo";
    ans3="1945";
    ans4="2011";

    if(s1==ans1 && s2==ans2 && s3==ans3 && s4==ans4){
        window.location.href = "/home";      
    }
    else{

        alert("Your Answers are wrong please try again!!");
    }

}