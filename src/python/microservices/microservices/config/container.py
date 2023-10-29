import logging

from dependency_injector import containers, providers
from microservices.controller.greeter_servicer import GreeterServicer
from microservices.usecase.greeter_usecase import GreeterUsecase

# def repository_factory_func(session) -> RepositoryFactory:
#     return RepositoryFactory(session)


logger = logging.getLogger(__name__)


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
    greeter_usecase = GreeterUsecase()
    greeter_servicer = providers.Singleton(
        GreeterServicer,
        greeter_usecase,
    )
