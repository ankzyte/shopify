let profileLink = document.querySelector(".profile");
let addressLink = document.querySelector(".address");
let currentUrl = window.location.pathname;
let address = document.querySelectorAll(".address-number");

for(let i=1;i<=address.length;i++){
    address[i-1].innerText = `${i}`;
}

if(currentUrl=="/profile/"){
    if(addressLink.classList.contains("active")){
        addressLink.classList.remove("active");
    }
    profileLink.classList.add("active");
}
else if(currentUrl=="/address/"){
    if(profileLink.classList.contains("active")){
        profileLink.classList.remove("active");
    }
    addressLink.classList.add("active");
}
