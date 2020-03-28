# NetworkTest

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e39e14dd853f4d4c9956a70c480c5fb9)](https://www.codacy.com/manual/DSuveges/NetworkTest?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DSuveges/NetworkTest&amp;utm_campaign=Badge_Grade)

This small project was motivated by recent problems with our internet access. 
These outages occurs randomly and their lengths were varying from less than a minute to half hour. 
This is a extremely annoying behavior and I have decided to monitor our internet service for a few days so I can enforce my complaints with measured data. 

### Approach

I have written a small Python Flask application that pings the rooter and remote server defined by the configuration file. 
The success of the ping is recorded in a simple SQLite database.

### TODO

1. Adding tools to analyze stored data + create network availability charts.
2. Improve the UI to visualize the network availability history.
    * Provide daily and weekly graph
    * The graph should also contain the number how many times the service went off and the total duration
3. Generate custom report based on the gathered data.
