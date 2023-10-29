from microservices.domain.user import User

from microservices.config.container import Container
from dependency_injector.wiring import Provide, inject
from microservices.controller.greeter_servicer import GreeterServicer
from helloworld.v1 import helloworld_pb2_grpc
# import  v1.helloworld_pb2_grpc

from pyaml_env import parse_config
import os
from importlib import resources

from concurrent import futures
from signal import SIGTERM, signal

import grpc
import logging

debug_mode = os.getenv("DEBUG_MODE")

# config
config_text = ""
if debug_mode:
    with open("microservices/config/config.yml", encoding="utf-8") as f:
        config_text = f.read()
else:
    config_text = resources.read_text("microservices.config", "config.yml")

print(config_text)
config_dict = parse_config(data=config_text)
print(config_dict)


# container
container = Container()
container.config.from_dict(config_dict)

print("hello")
print("hello")
# x = helloworld_pb2_grpc.GreeterServicer()
# print(x)

user = User()
print(user)

@inject
def run(
    greeter_servicer: GreeterServicer = Provide[Container.greeter_servicer],
):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(greeter_servicer, server)
    # calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    grpc_port = config_dict["app"]["grpcPort"]
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()

    # start metrics server
    # start_http_server(cfg.app.metricsPort)

    def handle_sigterm(*_):
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shut down gracefully")

    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()

def main():
    print("start")
    container = Container()
    container.wire(modules=[__name__])
    run()


if __name__ == "__main__":
    main()
