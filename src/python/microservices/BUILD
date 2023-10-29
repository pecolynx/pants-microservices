# python_requirement(
#     name="reqs",
#     requirements=[
#         "grpcio==1.59.0",
#         "dependency-injector==4.41.0",
#         "protobuf==4.24.4",
#         "pyaml-env==1.2.1",
#     ],
# )

python_sources(
    name="src",
    resolve="microservices",
    dependencies=[
        # "src/python/microservices/microservices",
        # "src/python/microservices/microservices/domain",
        # "src/python/microservices/microservices/controller",
        # "3rdparty/python:reqs#grpciox",
        # "3rdparty/python:reqs#protobuf",
        # "3rdparty/python:reqs#pyaml-env",

        # "3rdparty/python:reqs#dependency-injector",

        "src/python/microservices/microservices/**/*.py",
    ]
)

pex_binary(
    name="microservices",
    resolve="microservices",
    entry_point="microservices/main.py",
    dependencies=[
        ":src",
    ],
    restartable=True,
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="microservices",
)

# poetry_requirements(
#     name="poetry",
# )

# python_sources(
#     name="pkg",
#     dependencies=[
#         "3rdparty/python:grpc#grpcio",
#     ]
# )
