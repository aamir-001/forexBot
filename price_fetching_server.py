import time
import requests
import grpc
from concurrent import futures
import threading

import service_pb2
import service_pb2_grpc

class MyService(service_pb2_grpc.MyServiceServicer):
    def __init__(self):
        self.result_container = {}

    def fetch_usd_chf_price(self):
        try:
            response = requests.get(
                'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CHF&apikey=000')

            response.raise_for_status()

            self.result_container['usd_chf'] = response.json()
        except requests.RequestException as e:
            self.result_container['error'] = str(e)

    def fetch_eur_usd_price(self):
        try:
            response = requests.get(
                'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=000')

            response.raise_for_status()

            self.result_container['eur_usd'] = response.json()
        except requests.RequestException as e:
            self.result_container['error'] = str(e)

    def fetch_chf_eur_price(self):
        try:
            response = requests.get(
                'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=CHF&to_currency=EUR&apikey=000')

            response.raise_for_status()

            self.result_container['chf_eur'] = response.json()
        except requests.RequestException as e:
            self.result_container['error'] = str(e)

    def StreamData(self, request, context):
        try:
            while True:
                # start_time = time.time()

                # Start a thread to fetch data
                usd_chf_thread = threading.Thread(target=self.fetch_usd_chf_price)
                usd_chf_thread.start()
                eur_usd_thread = threading.Thread(target=self.fetch_eur_usd_price)
                eur_usd_thread.start()
                chf_eur_thread = threading.Thread(target=self.fetch_chf_eur_price)
                chf_eur_thread.start()

                usd_chf_thread.join()
                eur_usd_thread.join()
                chf_eur_thread.join()

                print(self.result_container.get('usd_chf', {}))
                # Create and yield the response message
                response = service_pb2.Response(
                    usd_chf = self.result_container.get('usd_chf', {})['Realtime Currency Exchange Rate']['5. Exchange Rate'],
                    eur_usd = self.result_container.get('eur_usd', {})['Realtime Currency Exchange Rate']['5. Exchange Rate'],
                    chf_eur = self.result_container.get('chf_eur', {})['Realtime Currency Exchange Rate']['5. Exchange Rate']
                )
                yield response

                # end_time = time.time()
                # duration = end_time - start_time
                # print(f"Time taken for execution: {duration:.2f} seconds")

                time.sleep(3)

        except Exception as e:
            context.set_details(f'Error: {e}')
            context.set_code(grpc.StatusCode.INTERNAL)
            return

def serve():
    # Set up the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
