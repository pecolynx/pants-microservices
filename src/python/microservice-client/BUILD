# python_requirement(
#     name="reqs",
#     requirements=[
#         "grpcio==1.59.0",
#     ],
# )

# poetry_requirements(
#     name="poetry",
# )

python_sources(
    name="src",
    dependencies=[
        # "src/python/microservices/microservices",
        # "src/python/microservices/microservices/domain",
        # "src/python/microservices/microservices/controller",
        # "3rdparty/python:reqs#grpciox",
        # "3rdparty/python:reqs#protobuf",
        # "3rdparty/python:reqs#pyaml-env",

        # "3rdparty/python:reqs#dependency-injector",

        "src/python/microservice-client/microservice_client/**/*.py",
    ]
)

pex_binary(
    name="microservice-client",
    entry_point="microservice_client/main.py",
    dependencies=[
        ":src",
    ],
    restartable=True,
)
