# Animal Adoption 

## First time running
create environment
```
py -3 -m venv .venv
```

activate environment
```
 .venv\Scripts\activate
```
run dependencies
```
pip install -r requirements.txt
```

## How to run
```cmd
set FLASK_APP=src
flask run
```

## Test
run this code initiate testing  
```cmd
pytest
```
 b

## Docker
```
docker build -t animal-adoption .
```

```
 docker run -it --rm --name animal-adoption
 ```


 Migrate db
 ```
 flask db upgrade
 ```