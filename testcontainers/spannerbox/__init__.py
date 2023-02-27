from typing import Any

from testcontainers.core.container import DockerContainer

_SPANNERBOX_DEFAULT_IMAGE = "iromli/spannerbox:1.0.1"


class SpannerboxContainer(DockerContainer):  # type: ignore
    """
    Basic container object to spin up Spannerbox.

    See https://github.com/iromli/docker-spannerbox for details.

    Example:

        The example spins up a Spannerbox container and configure it.

        .. doctest::

            >>> from testcontainers.spannerbox import SpannerboxContainer

            >>> with SpannerboxContainer() as container:
            ...     project_id = container.env["SPANNER_PROJECT_ID"]
            >>> project_id
            'test-project'
    """

    def __init__(  # noqa: D107
        self,
        image: str = _SPANNERBOX_DEFAULT_IMAGE,
        project_id: str = "test-project",
        instance_id: str = "test-instance",
        database_id: str = "test-database",
        **kwargs: dict[str, Any],
    ) -> None:
        super().__init__(image, **kwargs)
        self.with_env("SPANNER_PROJECT_ID", project_id)
        self.with_env("SPANNER_INSTANCE_ID", instance_id)
        self.with_env("SPANNER_DATABASE_ID", database_id)

    def start(self) -> "SpannerboxContainer":  # noqa: D102
        super().start()
        return self
