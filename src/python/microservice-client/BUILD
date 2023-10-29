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
    resolve="microservice-client",
    dependencies=[
        "src/python/microservice-client/microservice_client/**/*.py",
    ]
)

pex_binary(
    name="microservice-client",
    resolve="microservice-client",
    entry_point="microservice_client/main.py",
    dependencies=[
        ":src",
    ],
    restartable=True,
)
