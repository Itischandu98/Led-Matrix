# Led-Matrix
Web page with flask for raspberry pi led matrix board control 

The main Idea is to use the snake game program that has been written in the ESP 8266 which can be found in https://github.com/Itischandu98/Snake-Game into a fully Flask webpage to run using raspberry pi which has multiple options you can choose form.

The current ideas for pages include snake game, scrolling text (which could be further developed to display any comments in youtube or twitch using its APIs), led matrix contorl with color picker, tictactoe, Pong and to Display time etc.

I tried to use this to control led strips for different project so added a lot of unnessary lines but it still works add few extra flask lines to be able to control from automation like ios app or siri automation commands.

The app.py is the main python program which communicates between the html pages all the pages are included in the template folder.

The html pages are created using jinja syntax which is an amazing language and reduces the requirement for using javascript for simple things.