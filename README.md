#Smile Detector
Overview
This is a Python script that uses OpenCV and haarcascade classifiers to detect faces and smiles in real-time from your webcam. When you smile, the script will print "Smiling" to the console. When you frown, the script will print "Frowning". If you have a neutral expression, the script will print "Neutral".

Installation
Clone the repository: git clone https://github.com/your-username/smile-detector.git
Navigate to the project directory: cd smile-detector
Create a virtual environment: python -m venv env
Activate the virtual environment:
For Windows: env\Scripts\activate
For Mac/Linux: source env/bin/activate
Install the required libraries: pip install -r requirements.txt
Usage
Make sure your webcam is connected and functional
Activate the virtual environment:
For Windows: env\Scripts\activate
For Mac/Linux: source env/bin/activate
Run the script: python smile_detector.py
Smile and see the script's output in the console!
Configuration
The smile_detector.py script uses the haarcascade classifiers located in the haarcascades folder. If you want to use different classifiers

