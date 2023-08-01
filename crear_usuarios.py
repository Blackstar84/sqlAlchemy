import json
from faker import Faker
import random

def generate_random_json_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        name = fake.name()
        age = random.randint(18, 100)
        country = fake.country()
        email = fake.email()
        gender = random.choice(['male', 'female'])
        
        record = {
            "age": str(age),
            "country": country,
            "email": email,
            "gender": gender,
            "name": name
        }
        data.append(record)
    
    return data

if __name__ == '__main__':
    num_records = 3  # You can change this to generate more records
    random_json_data = generate_random_json_data(num_records)
    print(json.dumps(random_json_data, indent=4))
    
# Explicación del Código línea por línea

# Claro, con gusto te explico qué hace cada línea del código:

# 1. `import json`: Importa el módulo `json`, que proporciona funcionalidades para trabajar con datos en formato JSON.

# 2. `from faker import Faker`: Importa la clase `Faker` del módulo `faker`. `faker` es una biblioteca que permite generar datos ficticios, como nombres, direcciones, correos electrónicos, etc., útiles para pruebas y ejemplos.

# 3. `import random`: Importa el módulo `random`, que proporciona funcionalidades para generar números aleatorios y seleccionar elementos de secuencias de manera aleatoria.

# 4. `def generate_random_json_data(num_records):`: Define una función llamada `generate_random_json_data` que acepta un argumento `num_records`, que indica el número de registros o elementos JSON que se generarán.

# 5. `fake = Faker()`: Crea una instancia de la clase `Faker` y la asigna a la variable `fake`. Esta instancia se utilizará para generar datos ficticios en el bucle que sigue.

# 6. `data = []`: Inicializa una lista vacía llamada `data`. En esta lista se almacenarán los registros JSON generados.

# 7. `for _ in range(num_records):`: Inicia un bucle que se repetirá `num_records` veces, generando tantos registros JSON como se haya especificado.

# 8. `name = fake.name()`: Genera un nombre ficticio aleatorio utilizando el objeto `fake`, que es una instancia de `Faker`. El nombre generado se asigna a la variable `name`.

# 9. `age = random.randint(18, 100)`: Genera un número entero aleatorio entre 18 y 100 (ambos inclusive) y lo asigna a la variable `age`.

# 10. `country = fake.country()`: Genera un país ficticio aleatorio utilizando `fake` y lo asigna a la variable `country`.

# 11. `email = fake.email()`: Genera una dirección de correo electrónico ficticia aleatoria utilizando `fake` y lo asigna a la variable `email`.

# 12. `gender = random.choice(['male', 'female'])`: Selecciona aleatoriamente una cadena de género ('male' o 'female') de la lista proporcionada y lo asigna a la variable `gender`.

# 13. `record = {...}`: Crea un diccionario `record` que contiene los datos generados en los pasos anteriores. Este diccionario representa un registro JSON con claves "age", "country", "email", "gender" y "name".

# 14. `data.append(record)`: Agrega el registro `record` a la lista `data`.

# 15. `return data`: La función devuelve la lista `data` que contiene los registros JSON generados.

# 16. `if __name__ == '__main__':`: Esta es una construcción que verifica si el archivo es el programa principal que se está ejecutando, no importado como un módulo en otro script. Si se cumple esta condición, el bloque de código dentro de este `if` se ejecuta.

# 17. `num_records = 3`: Establece el número de registros JSON que se generarán en la variable `num_records`. Puedes cambiar este valor para generar más o menos registros.

# 18. `random_json_data = generate_random_json_data(num_records)`: Llama a la función `generate_random_json_data` con el valor de `num_records` y almacena el resultado en la variable `random_json_data`. Esta variable contendrá la lista de registros JSON generados.

# 19. `print(json.dumps(random_json_data, indent=4))`: Imprime la lista de registros JSON generados en un formato más legible, utilizando `json.dumps()` para convertir la lista a una cadena JSON con sangrías (indent=4). Esto permite visualizar el resultado de manera organizada en la consola.
   
