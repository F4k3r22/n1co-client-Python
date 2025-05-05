import http.client

class n1coClient:
    def __init__(self, api_key, host="api.n1co.com"):
        self.api_key = api_key
        self.host = host
        self.headers = {
            'Content-Type': "application/json",
            'Authorization': self.api_key
        }
        print(f"Cliente n1co inicializado con host: {self.host}")
        print(f"Headers configurados: {self.headers}")

    def charges(self, payload):
        try:
            print("\n--- INICIANDO SOLICITUD DE CARGO ---")
            print(f"Host destino: {self.host}")
            print(f"Endpoint: /api/v2/Charges")
            print(f"Payload a enviar: {payload}")
            
            print("\nEstableciendo conexión HTTPS...")
            conn = http.client.HTTPSConnection(self.host)
            
            print("Enviando solicitud POST...")
            conn.request("POST", "/api/v2/Charges", payload, headers=self.headers)
            
            print("Esperando respuesta...")
            res = conn.getresponse()
            
            print(f"Respuesta recibida - Código de estado: {res.status} {res.reason}")
            print(f"Headers de respuesta: {res.getheaders()}")
            
            response_data = res.read()
            print("\n--- RESPUESTA DEL SERVIDOR ---")
            print(response_data.decode("utf-8"))
            print("--- FIN DE RESPUESTA ---\n")
            
            return response_data.decode("utf-8")
        except Exception as e:
            print("\n--- ERROR EN LA SOLICITUD ---")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Detalles del error: {e}")
            print("--- FIN DEL ERROR ---\n")
            return None

    def collections(self):
        try:
            conn = http.client.HTTPSConnection(self.host)

            conn.request("GET", "/api/v2/Collections", headers=self.headers)

            res = conn.getresponse()
            data = res.read()

            return data.decode("utf-8")
        
        except Exception as e:
            print("\n--- ERROR EN LA SOLICITUD ---")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Detalles del error: {e}")
            print("--- FIN DEL ERROR ---\n")
            return None

    def get_orders_id(self, id):
        try:
            conn = http.client.HTTPSConnection(self.host)

            conn.request("GET", f"/api/v2/Orders/{id}", headers=self.headers)

            res = conn.getresponse()
            data = res.read()

            return data.decode("utf-8")

        except Exception as e:
            print("\n--- ERROR EN LA SOLICITUD ---")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Detalles del error: {e}")
            print("--- FIN DEL ERROR ---\n")
            return None

    def get_orders_id_shipment(self, id):
        try:
            conn = http.client.HTTPSConnection(self.host)

            conn.request("GET", f"/api/v2/Orders/{id}/Shipment", headers=self.headers)

            res = conn.getresponse()
            data = res.read()

            return data.decode("utf-8")

        except Exception as e:
            print("\n--- ERROR EN LA SOLICITUD ---")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Detalles del error: {e}")
            print("--- FIN DEL ERROR ---\n")
            return None

    def get_orders(self):
        try:
            conn = http.client.HTTPSConnection(self.host)

            conn.request("GET", f"/api/v2/Orders", headers=self.headers)

            res = conn.getresponse()
            data = res.read()

            return data.decode("utf-8")

        except Exception as e:
            print("\n--- ERROR EN LA SOLICITUD ---")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Detalles del error: {e}")
            print("--- FIN DEL ERROR ---\n")
            return None