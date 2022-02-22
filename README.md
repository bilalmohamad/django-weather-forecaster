# Django Weather Forecaster
This application was created using the Django framework!
To run this application, you first must ensure that Python is installed on your computer.

## Make the project
This project can be cloned by running the following command:
```
git clone https://github.com/sahilpatel09/WeatherForecastOpenWeatherMap.git
```

This will add the project to your local machine.

## Create a Virtual Environment
If you do not wish to install the project's dependencies to your computer, it is recommended to create a virtual environment.
This can be completed by running the following commands:

#### MacOS / Linux
```
virtualenv --no-site-packages env
source env/bin/activate
```
#### Windows
```
virtualenv env
.\env\Scripts\activate
```

## Installing Dependencies
To install the required dependencies needed to run the project, ensure that the current directory is .../django-weather-forecaster/WeatherApp/

Then run the following command:
```
pip install -r requirements.txt
```

## Running the Project
To run the project, make sure the current directory is .../django-weather-forecaster/WeatherApp/

Then run the following command:
```
python manage.py runserver
```

Open a web browser and enter the url:
```
localhost:8000
```
