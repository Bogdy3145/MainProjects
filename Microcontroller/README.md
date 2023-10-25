SIDE PROJECT

https://youtu.be/Ma4ArkK9BAE

This is a robot that me and 2 other friends built.

Used language: C

While building this robot I learned about the basics and a bit more of what that microcontroller can do.

This robot has inside 2 STM32 Nucleo microcontrollers and this is just a result of what we learned throughout the whole project.
My contribution in the robot that you can see is:
    -setting up the connection between the controller and the car
        -initially I used a basic app and connected it through bluetooth to a bluetooth module on the board, but that was too easy so I changed to that big controller you see in the video
        -the controller is officially used for flying drones. The communication this time is made through RF
    -taking the input from the controller and giving physical functionalities
    -giving power to the wheels based on the controller (one of the sticks is the power (kindof like a gear-mechanism) and the other is the acceleration)
    -reading data from ultra-sound distance sensors and making sure the robot wouldn't bump into anything

That's pretty much it, enjoy ;)
