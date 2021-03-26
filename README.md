# Web_Cam
Solution for cutting frames from video

-Python file
-Jupyter notebook service

## What you can do with this app

- Extract frames from video file at 15 second intervals

### What to do for this

- Create a directory for the program, clone the repo into it and set the virtual environment
- Put your video file in the project folder
- Create a directory in the project folder for sliced files (instead of jpeg)
- In 'camweb' file replace video file name with your file and replace 'jpeg' with your directory name
- 15000 in the code is the interval of 15 seconds between sliced frames. Change this value to increase or decrease the spacing. Focus on the size of the video file!
- Run 'jupyter notebook' at the command line
- Open the specified page in the browser
- In the window that opens, Click on the right 'New' and then 'Python 3'
- Paste the contents of the 'camweb' file (via cp) into the opened line 'input'
- Click 'Start'
- Your frames from the video file are recorded in the directory for sliced files.
