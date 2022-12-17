from django.shortcuts import render
from django.http import HttpResponse
import openai

def ajax(request):
    message = request.GET["message"]
    openai.api_key = "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"
    response = openai.Completion.create(model="text-davinci-003", prompt=message, temperature=0, max_tokens=4000)
    print(response)
    return HttpResponse(response["choices"])

def index(request):

    page_html =    """
        <style>
            @font-face {
            font-family: Inter;
            src: url(static/inter.ttf);
            }


            #chat-window {
            height: calc(100% - 40px);
            overflow: auto;
            background-color: transparent;
            }

            #input-box {
            height: 40px;
            background-color: transparent;
            display: flex;
            align-items: center;
            padding: 0 10px;
            }

            #input-box input[type="text"] {
            width: 100%;
            height: 100%;
            border: none;
            outline: none;
            background-color: transparent;
            color: white;
            font-size: 16px;
            }
        </style>

        <body style="background-color: #121212; color: white; font-family: Inter; font-size: 18px; opacity:0.87">
            <div id="chat-window"></div>

            <div id="input-box">
            <input id="message" type="text" placeholder="Write something here..." onkeypress=clickPress(event)>
            </div>
        </body>

        <script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.js"></script>
        <script>

            load_response("Hi, I am Craig.");

            function load_response(response) {
                document.getElementById('chat-window').innerHTML = "";
                var sentence = new String(response).replace('\\n','').replace('\\n','').replaceAll('OpenAI','Craig')
                var sentenceArray = sentence.split('');
                var sentenceLength = sentenceArray.length;
                var sentenceIndex = 0;
                var sentenceInterval = setInterval(function() {
                if (sentenceIndex < sentenceLength) {
                    if (sentenceArray[sentenceIndex] == "\\n") {
                        document.getElementById("chat-window").innerHTML += "<br>";
                        sentenceIndex++;
                    } else if (sentenceArray[sentenceIndex] == " ") {
                        document.getElementById("chat-window").innerHTML += "&nbsp";
                        sentenceIndex++;
                    } else {
                        document.getElementById("chat-window").innerHTML += sentenceArray[sentenceIndex];
                        sentenceIndex++;
                    }
                } else {

                }
                }, 50);
            }

            function clickPress(event) {
                if (event.keyCode == 13) {
                    message = document.getElementById("message").value
                    if (message != "") {
                        document.getElementById("message").value = ""
                        $.get('ajax/', {"message":message}, function (data, textStatus, jqXHR) {
                            response = JSON.parse(data)["text"];
                            load_response(response);
                        });
                    }
                }
            }
        </script>
        """
        
    return HttpResponse (page_html)