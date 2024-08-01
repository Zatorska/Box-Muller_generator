## Box-Muller Generator

This project addresses the following task:
>_"The company specializing in the mining industry decided to invest in data analytical machines. There is no collected data, but the company wants to have results of analysis ASAP. It is therefore necessary to generate random numbers which let us check if machines work correctly."_

In this project, I created a Box-Muller random number generator and tested its correctness using:
* D'Agostino Pearson normality test,
* Kolmogorov-Smirnov normality test,
* Quantile charts.

**Code written in **Python**.**

### Versions
This repository contains two versions of the Box-Muller generator:

1. **Version 1 (v1)**: Implemented in a Jupyter Notebook (`box_muller.ipynb`). This version provides a step-by-step explanation and description of the code and its functionality.

2. **Version 2 (v2)**: Implemented using Object-Oriented Programming (OOP) principles. This version includes:
   - `box_muller.py` which contains the class definition.
   - `main.py` which serves as the entry point to run the application and demonstrates usage.

**How Box-Muller Generator Works**  
In simple terms, it takes two samples from the uniform distribution on the interval and maps them to two standard, normally distributed samples. The differences before and after the Box-Muller transformation can be seen below:

![](Images/bm1.png)

An interesting Box-Muller visualization can be found [here](https://upload.wikimedia.org/wikipedia/commons/1/1f/Box-Muller_transform_visualisation.svg).  
More information about the Box-Muller transformation can be found [here](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform).

