import grpc
import service_pb2
import service_pb2_grpc
from decimal import Decimal, getcontext


def run():
    getcontext().prec = 200

    initial_amount = Decimal('1000.0')
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = service_pb2_grpc.MyServiceStub(channel)
            response_iterator = stub.StreamData(service_pb2.Request(query='example'))
            for response in response_iterator:

                print(response)
                usd_chf = Decimal(response.usd_chf if response.usd_chf is not None else '0')
                chf_eur = Decimal(response.chf_eur if response.chf_eur is not None else '0')
                eur_usd = Decimal(response.eur_usd if response.eur_usd is not None else '0')

                # Calculate if trade is feasible
                product = usd_chf * chf_eur * eur_usd
                if product > Decimal('1.0001'):
                    initial_amount *= product

                #execute trade

            # Format the final amount to avoid scientific notation
            final_amount_str = '{:f}'.format(initial_amount)
            print(f"Final amount = {final_amount_str}")

    except grpc.RpcError as e:
        print(f"gRPC error occurred: {e.code()} - {e.details()}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    run()
