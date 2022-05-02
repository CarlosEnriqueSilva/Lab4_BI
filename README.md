# Laboratorio 4 BI
## Integrantes:
- Sara Calle
- Carlos Silva
- Juliana Velasco

## Instrucciones de instalación e inicialización:
1. Instalar los requerimientos en el archivo "requirements.txt"
2. Abrir la consola e ir a la direccion de la carpeta Lab4 - API
3. Asegurarse que en la carpeta assets este el archivo modelo.joblib. Si no esta correr el modelo de la carpeta Lab 4 -Pipeline y pegar el resultado en dicha ubicacion.
4. Correr el siguiente comando -> "uvicorn main:app --reload"

## Instrucciones URL predicción
1. Abrir Postman
2. Seleccionar el metodo POST
3. Ingresar la siguiente URL -> "http://127.0.0.1:8000/predict"
4. Seleccionar la pestaña Body
5. Seleccionar como tipo de cuerpo "raw"
6. Seleccionar formato JSON
7. Incluir en el espacio los datos que se utilizaran para predecir en el siguiente formato:
{
  "adult_mortality": 285,
  "infant_deaths": 25,
  "alcohol": 1.35,
  "percentage_expenditure": 8.931827297,
  "hepatitis_B": 73,
  "measles": 217,
  "bmi": 19.7,
  "under_five_deaths": 40,
  "polio": 75,
  "total_expenditure": 4.63,
  "diphtheria": 73,
  "hiv_aids": 2.1,
  "GDP": 519.2922847,
  "population": 752555,
  "thinness_10_19_years": 9.1,
  "thinness_5_9_years": 9,
  "income_composition_of_resources": 0.416,
  "schooling": 7.7
}
8. Dar en el boton "Send"
9. La respuesta es la variable predicha

## Instrucciones URL R^2
1. Abrir Postman
2. Seleccionar el metodo POST
3. Ingresar la siguiente URL -> "http://127.0.0.1:8000/evaluate"
4. Seleccionar la pestaña Body
5. Seleccionar como tipo de cuerpo "raw"
6. Seleccionar formato JSON
7. Incluir en el espacio los datos que se utilizaran para predecir en el siguiente formato:
{
  "datos": [
      {
    "life_expectancy": 65,
    "adult_mortality": 263,
    "infant_deaths": 62,
    "alcohol": 0.01,
    "percentage_expenditure": 71.27962362,
    "hepatitis_B": 65,
    "measles": 1154,
    "bmi": 19.1,
    "under_five_deaths": 83,
    "polio": 6,
    "total_expenditure": 8.16,
    "diphtheria": 65,
    "hiv_aids": 0.1,
    "gdp": 584.25921,
    "population": 33736494,
    "thinness_10_19_years": 17.2,
    "thinness_5_9_years": 17.3,
    "income_composition_of_resources": 0.479,
    "schooling": 10.1
  },
  {
    "life_expectancy": 59.9,
    "adult_mortality": 271,
    "infant_deaths": 64,
    "alcohol": 0.01,
    "percentage_expenditure": 73.52358168,
    "hepatitis_B": 62,
    "measles": 492,
    "bmi": 18.6,
    "under_five_deaths": 86,
    "polio": 58,
    "total_expenditure": 8.18,
    "diphtheria": 62,
    "hiv_aids": 0.1,
    "gdp": 612.696514,
    "population": 327582,
    "thinness_10_19_years": 17.5,
    "thinness_5_9_years": 17.5,
    "income_composition_of_resources": 0.476,
    "schooling": 10
  }
]
8. Dar en el boton "Send"
9. La respuesta es el valor de R^2 para esos datos
