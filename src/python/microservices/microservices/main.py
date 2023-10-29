import logging
import os
from concurrent import futures
from importlib import resources
from signal import SIGTERM, signal

import grpc
from dependency_injector.wiring import Provide, inject
from microservices.config.container import Container
from microservices.controller.greeter_servicer import GreeterServicer
from microservices_helloworld.v1 import helloworld_pb2_grpc
from pyaml_env import parse_config

logger = logging.getLogger(__name__)


@inject
def run(
    grpc_port: int,
    greeter_servicer: GreeterServicer = Provide[Container.greeter_servicer],
):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(greeter_servicer, server)
    # calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    # grpc_port = config_dict["app"]["grpcPort"]
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

    # print("start")
    container = Container()
    container.config.from_dict(config_dict)
    container.wire(modules=[__name__])
    run(grpc_port=int(config_dict["app"]["grpcPort"]))


if __name__ == "__main__":
    main()
