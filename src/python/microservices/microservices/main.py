from microservices.domain.user import User

# from microservices.config.container import Container
from helloworld.v1 import helloworld_pb2_grpc
# from protos.helloworld.v1 import helloworld_pb2_grpc
# import  v1.helloworld_pb2_grpc

print("hello")
print("hello")
x = helloworld_pb2_grpc.GreeterServicer()
print(x)

user = User()
print(user)


# @inject
# def run(
#     calc_server: CalcServer = Provide[Container.calc_server],
# ):
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
#     # calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
#     calc_pb2_grpc.add_CalculatorServicer_to_server(calc_server, server)
#     server.add_insecure_port(f"[::]:{cfg.app.grpcPort}")
#     server.start()

#     # start metrics server
#     start_http_server(cfg.app.metricsPort)

#     def handle_sigterm(*_):
#         print("Received shutdown signal")
#         all_rpcs_done_event = server.stop(30)
#         all_rpcs_done_event.wait(30)
#         print("Shut down gracefully")

#     signal(SIGTERM, handle_sigterm)
#     server.wait_for_termination()

def main():
    print("start")
    container = Container()
    container.wire(modules=[__name__])
    # run()


if __name__ == "__main__":
    main()
