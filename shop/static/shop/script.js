let profileLink = document.querySelector(".profile");
let addressLink = document.querySelector(".address");
let currentUrl = window.location.pathname;
let address = document.querySelectorAll(".address-number");
let images = document.querySelectorAll(".slider img");
let dots = document.querySelectorAll(".dot");
let price = document.querySelectorAll(".price");
let sum = 0;
let amount = document.querySelector("#amount");
let totalamount = document.querySelector('#total-amount');

for(let i=0;i<dots.length;i++){
    dots[i].addEventListener("click",()=>{
        for(let i=0;i<dots.length;i++){
            dots[i].classList.remove("active");
            images[i].style.opacity=0;
        }
        dots[i].classList.add("active");
        images[i].style.opacity=1;
        j=i;
    });
}

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

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name matches the specified name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                // Extract and decode the cookie value
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function() {
    // Find the button element by its ID

    var createInstanceBtn = document.getElementById('create-instance-btn');
        
        // Add an event listener to the button click event
    createInstanceBtn.addEventListener('click', function() {
        
        if(createInstanceBtn.className=='add-to-cart'){
            console.log(createInstanceBtn.className);
            var csrftoken = getCookie('csrftoken');
            // Create the fetch request
            fetch("addtocart/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
            })
            .then(function(response) {
                    // Check if the request was successful
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                    // Parse the JSON response
                return response.json();
            })
            .then(function(data) {
                    // Handle the data received from the server
                createInstanceBtn.classList.remove('add-to-cart');
                createInstanceBtn.classList.add('goto-cart');
                createInstanceBtn.innerText = 'Goto Cart';
                console.log(data.message);  // Log success message
            })
            .catch(function(error) {
                    // Handle any errors that occurred during the fetch request
                console.error('There was a problem with the fetch operation:', error);
            });
        }     
        else{
            window.location.href = '/user/showcart/';
        }   
    });
});

for(let i=0;i<price.length;i++){
    sum += Number(price[i].innerText);
}
amount.innerText = `Rs ${sum}`;
totalamount.innerText = `Rs ${sum+100}`;