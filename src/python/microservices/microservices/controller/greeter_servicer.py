from helloworld.v1 import helloworld_pb2_grpc
from helloworld.v1.helloworld_pb2 import HelloRequest, HelloReply
from microservices.usecase.greeter_usecase import GreeterUsecase


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self, greeter_usecase: GreeterUsecase):
        self.greeter_usecase = greeter_usecase

    def Add(self, request: HelloRequest, context) -> HelloReply:
        message = self.calc_usecgreeter_usecasease.greet(request.name)
        return HelloReply(message=message)
