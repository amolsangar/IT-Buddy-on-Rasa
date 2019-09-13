let status = document.getElementById('status');
let chatbox = document.getElementById('main-box');
let id = Math.floor(Math.random() * 1000 + 1);
let ul = document.getElementById('conversation');
let chat = document.getElementById("chat-container");
let input = document.getElementById("chat-input");
let fab = document.getElementById('fab');
let fab_close = document.getElementById('fab-close');

let user_id = uniqueID();

const url = 'http://localhost:5005';

var userid = 'default';
var userDetails = {};
function encodeEmail(emailid) {
    emailid = emailid.replace(/[@]/g, '%40');
    emailid = emailid.replace(/[.]/g, '%2E');
    emailid = emailid.replace(/[-]/g, '%2D');

    return emailid;
}

var fetchUserDetails = (function(emailid) {
    var executed = false;
    return function(emailid) {
        if (!executed) {
            executed = true;
            var emailid = encodeEmail(emailid);
            alert(emailid);

            var url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Clients?qualifier=(email%20like%20'"+emailid+"')&apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK";
            fetch(url, 
                {
                    method: 'GET',
                    headers: {
                            'Content-Type': 'application/json',
                    }
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (responses) {
                    console.log(responses);
                    if (responses) {
                        userid = responses[0]['username'];
                    } 
                    else {
                        console.log("Chatbot Error: Unable to fetch user details.");
                    }
                    return responses;
                })
                .then(function (responses) {
                    console.log(responses);
                    if (responses) {
                        respond(JSON.stringify(responses));
                    } 
                    else {
                        console.log("Chatbot Error: Unable to fetch user details.");
                    }
                })
                .catch(function (err) {
                    console.log("Chatbot Error: Technical issue present. Users details not fetched. Try again later :)");
                }); 
        }
    };
})();

//fetchUserDetails('amol.sangar@t-systems.com');

//console.log(JSON.stringify(obj));
let promise = new Promise(function(resolve, reject) {
    setTimeout(() => {

        var obj = JSON.parse(`[{
            "id": 353,
            "type": "Client",
            "email": "aishwarya.patil@t-systems.com",
            "firstName": "Aishwarya",
            "lastName": "Patil",
            "notes": null,
            "phone": null,
            "phone2": null,
            "department": {
                "id": 33,
                "type": "Department",
                "name": "SAPDelivery-Amol Kalgaonkar-47200030"
            },
            "location": {
                "id": 1,
                "type": "Location",
                "address": null,
                "city": null,
                "locationName": "PUNE-SHIVAJI NAGAR",
                "postalCode": null,
                "state": null,
                "priorityTypes": [],
                "useSpecificPriorities": false,
                "defaultPriorityTypeId": null
            },
            "room": null,
            "username": "A94799270",
            "companyName": "T-Systems ICT India Pvt. Ltd."
        }]`);
        resolve(obj);  
    }, 0);

});
promise.then(function(result) {
    //alert(JSON.stringify(result));
    userid = result[0]['username'];
    //respond(JSON.stringify(result));
});

//setTimeout(() => alert(userid), 100);;


input.addEventListener("keyup", function (event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("btn").click();
    }
});

window.onload = function () {
    fetch(`${url}`, {
        method: 'GET'
    })
        .then(function (response) {
            status.innerHTML = "<i class='fas fa-circle'></i> Online";
        })
        .catch(function (response) {
            status.innerHTML = "<i class='fas fa-circle' style='color:red'></i> Offline";
        })
}

function openchat() {
    chatbox.style.display = "block"
    fab.style.display = "none";
    fab_close.style.display = "block";
}

function closechat() {
    chatbox.style.display = "none";
    fab_close.style.display = "none";
    fab.style.display = "block";
}

function start(msg) {
    createSender(msg);
    document.getElementById('typing').style.display = "inline";
    respond(msg);
}

function speak(msg) {
    var speech = new SpeechSynthesisUtterance(msg);
    speech.voice = speechSynthesis.getVoices()[5];
    window.speechSynthesis.speak(speech);
}

function createSender(msg) {
        let li = document.createElement('li');
        li.appendChild(document.createTextNode(msg));
        li.className = "sender"
        ul.appendChild(li);
        document.getElementById('chat-input').value = "";
        chat.scrollTop = chat.scrollHeight;
}

function createResponder(msg) {
    let li = document.createElement('li');
    li.innerHTML = msg;
    if (voice() == true)
        speak(li.innerText);
    li.className = 'responder';
    ul.appendChild(li)
    chat.scrollTop = chat.scrollHeight;
}

function send() {
    let message = document.getElementById('chat-input').value;
    if (message != '') {
        createSender(message);
        document.getElementById('typing').style.display = "inline";
        if($(".suggestion")[0]) {
            $('.suggestion').remove();
        }
        respond(message);
    }
}

function respond(msg) {
    fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({
                "sender": userid,
                "message": msg
            })
        })
        .then(function (response) {
            document.getElementById('typing').style.display = "none";
            return response.json();
        })
        .then(function (responses) {
            console.log(responses);
            if (responses) {
                for (let response of responses) {
                    if(response.buttons) {
                        addSuggestion(response.buttons);
                    }
                    if(response.text) {
                        createResponder(response.text);
                    }
                    if(response.image) {
                        showImage(response.image);
                    }
            }
            } else {
                createResponder("Sorry, I'm having trouble understanding you, try asking me in an other way")
            }

        })
        .catch(function (err) {
            document.getElementById('typing').style.display = "none";
            createResponder("I'm having some technical issues. Try again later :)");
        });
}

function voice() {
    let speaker = document.getElementById('voice').checked;
    if (speaker == true)
        return true;
    else
        return false;
}

function listen() {
    let mic = document.getElementById('mic');
    mic.style.color = 'red';
    mic.className = 'animated pulse infinite';
    let hear = new webkitSpeechRecognition();
    hear.continuous = false;
    hear.lang = 'en-IN';
    hear.start();

    hear.onresult = function (e) {
        mic.style.color = 'black';
        mic.className = '';
        userVoiceText = e.results[0][0].transcript;
        hear.stop();
        createSender(userVoiceText);
        respond(userVoiceText);
    }
}

function addSuggestion(textToAdd) {
    setTimeout(function () {
        var suggestions = textToAdd;
        var suggLength = textToAdd.length;
        $('<p class="suggestion"></p>').appendTo('#conversation');
        // Loop through suggestions
        for (i = 0; i < suggLength; i++) {
            $('<button class="sugg-options" type="button" value="' + suggestions[i].payload + '">' + suggestions[i].title + '</button>').appendTo('.suggestion');
        }
        chat.scrollTop = chat.scrollHeight;
    }, 800);
}


// on click of suggestions get value and send to API.AI
$(document).on("click", ".suggestion button", function () {
    var text = this.innerText;
    createSender(text);
    var value = this.value;
    respond(value);
    $('.suggestion').remove();
});

function showImage(val) {

    setTimeout(function() {
        var BotResponse = '<p class="botResult"><img width="200" height="124" src="' + val + '/"></p><div class="clearfix"></div>';
        $(BotResponse).appendTo('#conversation');
        chat.scrollTop = chat.scrollHeight;
    }, 800);
}

function uniqueID(){
  function chr4(){
    return Math.random().toString(16).slice(-4);
  }
  return chr4() + chr4() +
    '-' + chr4() +
    '-' + chr4() +
    '-' + chr4() +
    '-' + chr4() + chr4() + chr4();
}

function createTicket(subject) {
    var url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets?apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK";
    fetch(url, {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "room": "",
          "emailClient": true,
          "emailTech": true,
          "emailTechGroupLevel": false,
          "emailGroupManager": false,
          "emailCc": false,
          "ccAddressesForTech": "",
          "emailBcc": false,
          "bccAddresses": "",
          "subject": subject,
          "detail": "Ticket raised from Chatbot.",
          "assignToCreatingTech": false,
          "problemtype": {
            "type": "ProblemType",
            "id": 149
          },
          "sendEmail": false,
          "location": {
            "type": "Location",
            "id": 1
          },
          "department": {
            "type": "Department",
            "id": 15
          },
          "clientReporter": {
            "type": "Client",
            "id": 172
          }
        })
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (responses) {
        console.log(responses);
        if (responses) {
            userid = responses[0]['username'];
        } 
        else {
            console.log("Chatbot Error: Unable to fetch user details.");
        }
        return responses;
    })
    .then(function (responses) {
        console.log(responses);
        if (responses) {
            respond(JSON.stringify(responses));
        } 
        else {
            console.log("Chatbot Error: Unable to fetch user details.");
        }
    })
    .catch(function (err) {
        console.log("Chatbot Error: Technical issue present. Users details not fetched. Try again later :)");
    });     
}