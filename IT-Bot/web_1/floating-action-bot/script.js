let status = document.getElementById('status');
let chatbox = document.getElementById('main-box');
let id = Math.floor(Math.random() * 1000 + 1);
let ul = document.getElementById('conversation');
let chat = document.getElementById("chat-container");
let input = document.getElementById("chat-input");
let fab = document.getElementById('fab');
let fab_close = document.getElementById('fab-close');
let chatbot = document.getElementById("chat-open");
chatbot.style.display = "none";

let user_id = uniqueID();

const url = 'http://localhost:5005';

var userid = 'default';

var sendEmail = (function(emailid) {
    var executed = false;
    return function(emailid) {
        if (!executed) {
            executed = true;

        //let message = "Email-Id: " + emailid;
        let message = `/email.id{"email": "${emailid}"}`

        fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({
                "sender": userid,
                "message": message
            })
        })
        .then(function (response) {
            document.getElementById('typing').style.display = "none";
            return response.json();
        })
        .then(function (responses) {
            //console.log(responses);
            if (responses) {
                for (let response of responses) {
                    if(response.text) {
                        userid = response.text;
                    }
                    //console.log(userid);
                }
            }
        })
        .finally(() => {
            respond('/say_hi');
            chatbot.style.display = "block";
        })
        .catch(function (err) {
            document.getElementById('typing').style.display = "none";
            createResponder("I'm having some technical issues. Try again later :)");
        });
        }
    };
})();


input.addEventListener("keyup", function (event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("btn").click();
    }
});

var emailid = 'amol.sangar@t-systems.com';
sendEmail(emailid);

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
            //console.log(responses);
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
            } 
            else {
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

/*window.onunload = function()
{
    if ((window.event.clientX < 0) || (window.event.clientY<0)) // close button
    {
        //do something on closing event
    }
    else if (window.event.altKey == true) // ALT + F4
    {
        //do something on closing event
    }
    else // for all other unload events
    {
        //do something on closing event
    }
}*/
