btn=document.getElementById('btn');

btn.onclick=()=>{
    s1=document.getElementById('s1').value.toLowerCase().trim();

    ans1="97";


    if(s1==ans1){
        window.location.href = "/finished";      
    }
    else{

        alert("Your Answer is wrong please try again!!");
    }

}