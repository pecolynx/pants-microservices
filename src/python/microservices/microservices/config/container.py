import logging

from dependency_injector import containers, providers

logger = logging.getLogger(__name__)
from helloworld.v1.helloworld_pb2_grpc import GreeterServicer


# def repository_factory_func(session) -> RepositoryFactory:
#     return RepositoryFactory(session)


class Container(containers.DeclarativeContainer):
    logger.info("Container")
    # wiring_config = containers.WiringConfiguration(
    #     packages=["microser.controller"]
    # )

    # config = providers.Configuration(yaml_files=[config.config_file_path])
    config = providers.Configuration()

    # print(config.db.url)

    # db = providers.Singleton(Database, db_url=config.db.url)
    # user_usecase_chart = providers.Factory(
    #     UserUsecaseChart,
    #     session_factory=db.provided.session,
    #     repository_factory_func=repository_factory_func,
    # )
    greeter_servicer = providers.Singleton(
        GreeterServicer,
    )
