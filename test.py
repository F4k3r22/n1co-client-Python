from nclient import n1coClient
import json

API_KEY = "93aab3a749aa8da9" # No es una API real, solo es para testear la repuesta y como demo del cliente

client = n1coClient(api_key=API_KEY)


data_charge = {
  "customer": {
    "id": "cliente123",
    "name": "Juan Pérez",
    "email": "juan@ejemplo.com",
    "phoneNumber": "+521234567890"
  },
  "order": {
    "id": "orden456",
    "amount": 299.99,
    "lineItems": [
      {
        "sku": "PROD001",
        "product": "Smartphone X10",
        "quantity": 1
      }
    ],
    "description": "Compra en línea",
    "name": "Pedido Web"
  },
  "cardId": "tarjeta789",
  "authenticationId": "auth123",
  "billingInfo": {
    "countryCode": "MX",
    "stateCode": "CDMX",
    "zipCode": "06700"
  },
  "locationCode": "tienda001",
  "metadata": [
    {
      "name": "origen",
      "value": "sitio_web"
    }
  ]
}

payload = json.dumps(data_charge)

response = client.charges(payload=payload)

if response:
    res = json.loads(response)
    print("Cargo procesado correctamente:")
    print(res)
else:
    print("Error al procesar el cargo")