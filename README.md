# Dataox

Test Task

#### Run project without Docker

Create virtual environment
```
python3 -m venv venv
```
Activate virtual enviroment
```
. venv/bin/activate
```
Install requirements
```
pip3 install -r requirements.txt
```
Create .env [example](https://github.com/skantrop/dataox/blob/master/.example)

Run
```
python3 app/main.py
```

#### Run w/ Docker
```
docker-compose build
docker-compose up
```
