# YHack2017 Tonalyzer
This is a web app that allows users input some English texts and analyzes the emotion within the texts with the help of IBM Watson Tone Analyzer API.

The basic functions are ready to use, but we are still struggling with using Twitter / Facebook's API to get users' post and analyze them.

To use this web app, simply go to the directory where the project located, input "export FLASK_APP=View.py" and "flask run", and finally open "http://localhost:5000/" in your browser.

Sample input:
"YHack2017 is awesome! I really enjoy the event and I hope I can come next time!"

Sample output:
"Document Tone": Joy, "Document Score": 0.895206
"YHack2017 is awesome!": Joy, 0.966739
"I really enjoy the event and I hope I can come next time!": Joy, 0.716822
"I really enjoy the event and I hope I can come next time!": Tentative, 0.716301
"I really enjoy the event and I hope I can come next time!": Analytical, 0.589295

Group members: Zixu (Shawn) Chen, Sid Sawhney
