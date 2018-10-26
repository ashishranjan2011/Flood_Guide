# Search

Problem:
In the situation of floods, if rescue operation is not conducted efficiently there can be great human loss. Suppose at location A there are 10 victims and in location B there are only 7 victims but in a highly miserable condition and at a distance greater than A. In these conditions B should be approached rather than A but generally anything can be done which may result in inability to rescue a large proportion of people.

Proposed Solution:.
The basic idea is to optimally conduct the process of rescuing the victims in the situation of a flood. The victims (group of victims) can submit their location and a quantitative description of their condition on the application. Using this data, the volunteer who has come to rescue would be continously informed about the next victim he should reach. This information is to be provided on the basis of certain parameter such as :
1. No. of people on that spot from where the request has been submitted.
2. No. of Woman/medically ill/disabled/old people/children at that spot.
3. Distance of that rescue site from volunteer.
4. Height of the spot from water level. (If water level is increasing)
5. Vicinity from available aid.

Based on these factors a priority would be calculated for a pirticular location of the rescuer. According to this priority the rescuer would be getring the location of next victim to be saved. In this way rescue operation can be conducted efficiently.

We are thinking to build this by having a Django server and make the app's frontend using Cordova framework or some other technology and process the data using Django REST API's. If we are successful in doing this we are also thinking to take the request of victim as voice and extract the values of parameters using maybe Microsoft entity recognition API's.
