# Meal Tracking App

## Overview

This application is a Meal Tracking program that allows users to record and retrieve data on their eating habits and help them live a healthier lifestyle. The app uses the popular 'macros' system that focuses on tracking carbs, fats, and proteins. These can be converted to calories with a 1:4. 1:9, and 1:4 ratio respectivley.

The app tracks how many servings of a specific food the user eats in a day, and stores that data in a separate JSON file that can be retrieved later by the system or sent to another program. If the user inputs a food item the program hasn't seen before, it will prompt the user for its name and macros information and save it to another file, adapting to the user over time.

The user can request information from the app on data from previous days, the current day, and specific food items.

>[Demonstration Video Coming soon](http://youtube.link.goes.here)

## Development Environment

I used VS Code and JDK to develop this program, using the Java programming language with the org.json library, along with the standard library.

## Useful Websites

* [Working with Java in VS Code](https://code.visualstudio.com/docs/java/java-project)
* [org.JSON Tutorial](https://www.tutorialspoint.com/org_json/org_json_jsonstringer.htm)
* [W3 Schools Java Tutorial](https://www.w3schools.com/java/java_intro.asp)

## Future Work

* Implement file I/O
* Converting JSON to Java object
