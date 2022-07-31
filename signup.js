let email_data=document.querySelector(".email");
let pass_data=document.querySelector(".password");
let name=document.querySelector(".name");

let signup=document.querySelector(".signup-button");
let close=document.querySelector(".close");
close.addEventListener("click",function(e){
    window.location.href = "signin.html";
})

signup.addEventListener("click",function(e){
    if(name.innerText ==""){
        alert("Enter Name Please!!");
        return;
    }
    else if(email_data.innerText ==""){
        alert("Enter Email Address!!");
        return;
    }
    else if(pass_data.value==""){
        alert("Enter Password!!");
        return;
    }
    else{
        let allTasks = localStorage.getItem("allTasks");
        if(allTasks == null) {
            let data = [{"name": name.innerText, "email": email_data.innerText, "password": pass_data.value}];
            localStorage.setItem("allTasks", JSON.stringify(data));
        } else {
            let data = JSON.parse(allTasks);
            data.push({"name": name.innerText, "email": email_data.innerText, "password": pass_data.value});
            localStorage.setItem("allTasks", JSON.stringify(data));
        }
        window.location.href = "signin.html";
    }
})