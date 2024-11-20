# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

## Description

Our project is an audio-based recognition system for activity. It's designed to analyze various sound events, such as clapping, snapping, and hitting a desk and classify them accordingly. The system leverages Docker for scalability, and operates in a containerized environment, as per the instructions.

# Build Badges

![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

![ML Client Workflow Status](https://github.com/software-students-fall2024/4-containers-super-awesome-team-name/actions/workflows/ml_client.yml/badge.svg?branch=main)

![Web App Workflow Status](https://github.com/software-students-fall2024/4-containers-super-awesome-team-name/actions/workflows/web_app.yml/badge.svg?branch=main)

## Configuration Instructions

Make sure you have Python 3.x downloaded from here:
https://www.python.org/downloads/

Then, download Docker Desktop at:
https://www.docker.com/products/docker-desktop/

After installing Docker and restarting computer, make sure Docker Desktop is running.

Then clone the GitHub respository onto your local machine with:

```
>>> git clone https://github.com/software-students-fall2024/4-containers-super-awesome-team-name
```

Open terminal in local cloned repository (path/to/4-containers-super-awesome-team-name) and run the following command:
```
>>> docker-compose up --build
```

Wait for build to finish then go to:
http://localhost:5000/

If you are using mac, you might need to disable airplay reciever as described here:
https://forums.developer.apple.com/forums/thread/682332

## Usage

The website will default to the home screen with an "Analyze Sound" button and "Records" button.

Analyze Sound takes user to a screen where the application will pick up sounds from user microphone (make sure microphone access is given).

When the circle under Tap to Listen is red, the app is not recording sound. Click the circle once and record a sound.

After finishing recording, tap the circle again and wait for the backend machine to classify the sound.

In the recording page, there is a button back to home page and a button to take user to "Records" page which is a history of user activity.

The user can then see all previous sounds that where classified, the classification of the sound, and the date the sound was recorded.

If the user wishes to do so, they can delete any sounds from the "Records" page using the delete button next to the sound.

All data will be stored in docker remotely and will be retrieved upon launch of application. If user wishes for something to be deleted, they must delete through the "Records" page.

## Optional Modification

This application can be used to classify more than just snaps, claps, and hits. 

To make the application classify any sounds of your choosing, input training data in .wav format into machine-learning-client/training_data. 

This will replace the training data for the back end machine learning with the sound of your choosing. 

To change the output syntax and classification names on the front end web application, further modification of variable names in web-app/templates and machine-learning-client/main.py will have to be done.

## Team members

- [Darren Zou](https://github.com/darrenzou)
- [Peter D'Angelo](https://github.com/dangelo729)
- [Gene Park](https://github.com/geneparkmcs)
- [Joseph Chege](https://github.com/JosephChege4)

# Acknowledgements

- The structure of docker-compose.yaml and our Dockerfile are based on the examples we were given in class: [Class Notes](https://knowledge.kitchen/content/courses/software-engineering/notes/containers/)
- When writing the tests, these sources were helpful to figure out mock methods, mock.patch, Flask config testing, and also just how the assertions should look 
    - [Librosa Package](https://librosa.org/doc/0.8.1/index.html#id1)
    - [Librosa Package](https://discuss.pytorch.org/t/mfcc-extracterted-by-librosa-pytorch/161180)-
    - [Python Mock](https://realpython.com/python-mock-library/)
    - [Flask Pytest](https://testdriven.io/blog/flask-pytest/)
    - [Flask Guide](https://flask.palletsprojects.com/en/stable)
    - [Pytest Mock Assert](https://pytest-with-eric.com/mocking/pytest-mock-assert-called/)
    - [Pytest Tutorial](https://www.geeksforgeeks.org/pytest-tutorial-testing-python-application-using-pytest/)
    - [Unit Testing](https://www.skillreactor.io/learn/unit-testing-in-backend-development/unit-testing-in-python-with-flask-and-pytest)