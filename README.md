# Columbus-Gym-Recommendation-Tool

## Overview
This is a simple `Python tool` that `helps users find gyms in Columbus, Ohio`, based on the type of gym they want.  
The user enters the first letter of a gym type, selects a matching type, and the program displays all gyms that match.

## Future Improvements
1. Right now, `this tool is simple and something I plan to build on`. Linear search works fine because there are not many gyms in Columbus (a few dozen). However, if the tool were scaled to the entire United States or globally, using a faster search method, such as a `hash `map, binary search, or a proper search engine, would be more effective.

2. The program currently uses fake gym data. In the future, I plan to implement an `API (similar to the Google Maps API)` to retrieve actual gym data and potentially `utilize AI` or another tool to automatically categorize gyms by type.

3. Eventually, I would also like to turn this command-line tool into a `simple web app` so it is easier for people to use.

4. Some of the logic in the program can be improved to adhere to best practices.


## Features
- Stores gym data in a list of dictionaries (Python data structure)
- Uses a linear search algorithm to find matching gyms
- Partial substring matching for gym types
- Input validation for both single-letter and full-string inputs
- Clean and simple CLI experience
- Modular Functions

## Technology Used
1. Python
2. Git and GitHub version control
3. Command Line Interface
5. ChatGPT `(to help generate fake gym data)`

## How to Run
1. With Python installed, clone or download the repository
2. Open a terminal in the project folder
3. Run with Main.py
