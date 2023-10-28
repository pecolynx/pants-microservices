# from grpc_server.proto import helloworld_pb2_grpc
# from grpc_server.proto.calc_pb2 import CalcRequest, CalcResponse
# from grpc_server.usecase.calc_usecase import CalcUseCase


# class HelloWorldServer(calc_pb2_grpc.CalculatorServicer):
#     def __init__(self, calc_usecase: CalcUseCase):
#         self.calc_usecase = calc_usecase

#     def Add(self, request: CalcRequest, context) -> CalcResponse:
#         print(f"{request.value1}")
#         result = self.calc_usecase.add(request.value1, request.value2)
#         return CalcResponse(result=result)
