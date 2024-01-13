# NBA Hall of Fame

Analyzed NBA Hall of Fame data, creating and deploying a Random Forest model to predict which players will get into Hall of Fame. Created Flask application and hosted on cloud via AWS Beanstalk so users can see how likely their favorite player is to get into Hall of Fame. 

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed the latest version of [Python](https://www.python.org/downloads/).
- You have installed [Pipenv](https://pipenv.pypa.io/en/latest/). You can install it using `pip install pipenv`.

## Installation and Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/tarunchinta/NBA-Hall-of-Fame.git
cd NBA-Hall-of-Fame
```

### 2. Set Up the Virtual Environment and Install Dependencies

Use Pipenv to create a virtual environment and install the required dependencies:

```bash
pipenv install
```

This command will create a virtual environment specific to this project and install all the dependencies listed in the `Pipfile`.

### 3. Activate the Virtual Environment

To activate the virtual environment and access the project's dependencies, run:

```bash
pipenv shell
```

### 4. Additional Setup

You need an API Key from API-NBA. Documentation is found below:
https://api-sports.io/documentation/nba/v2#section/Introduction

## Running the Project

```bash
python NBA-Hall-of-Fame-Initial-Analysis.ipynb
```

## Contributing to the Project

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b branch-name`.
3. Make your changes and commit them: `git commit -m 'commit-message'`.
4. Push to the original branch: `git push origin your-project-name/branch-name`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact me, you can reach me at `tarunc@utexas.edu`.