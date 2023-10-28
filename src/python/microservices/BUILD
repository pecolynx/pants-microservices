poetry_requirements(
    name="poetry",
)

pex_binary(
    name="microservices",
    entry_point="microservices/main.py",
    dependencies=[
        "src/python/microservices/microservices",
    ],
    restartable=True,
)


docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="microservices",
)
