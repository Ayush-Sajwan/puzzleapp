btn=document.getElementById('btn');

btn.onclick=()=>{
    book1=document.getElementById('book1').value.toLowerCase().trim();
    book2=document.getElementById('book2').value.toLowerCase().trim();
    book3=document.getElementById('book3').value.toLowerCase().trim();

    ans1="gk";
    ans2="science";
    ans3="maths";

    if(book1==ans1 && book2==ans2 && book3==ans3){
        window.location.href = "/university";      
    }
    else{

        alert("Your Answers are wrong please try again!!");
    }

}