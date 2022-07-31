let email_data=document.querySelector(".email");
let pass_data=document.querySelector(".password");

let signin=document.querySelector(".signin-button");
let close=document.querySelector(".close");

let c=0;
close.addEventListener("click",function(e){
    window.location.href = "main.html";
})
signin.addEventListener("click",function(e){
    if(email_data.innerText ==""){
        alert("Enter Email Address!!");
    }
    else if(pass_data.value ==""){
        alert("Enter Password!!");
        console.log(pass_data.innerText);
    }
   
    else{
        
        let allTasks = localStorage.getItem("allTasks");
        if(allTasks == null) {
            alert("Please Sign Up");
            return;
        }else{
            allTasks = JSON.parse(allTasks);
            for(let i = 0; i < allTasks.length; i++){
                if(email_data.innerText ==allTasks[i].email && pass_data.value ==allTasks[i].password){
                    window.location.href = "index.html";
                    c++;
                    return;
                }
            }
           
            
        }
        if(c==0){
            alert("Enter valid Email and Password !!");
        }
    }
})