import pytest


@pytest.mark.parametrize("env_mapping", [
    {
        "SPANNER_PROJECT_ID": "test-project",
        "SPANNER_INSTANCE_ID": "test-instance",
        "SPANNER_DATABASE_ID": "test-database",
    },
])
def test_docker_run_spannerbox(env_mapping):
    from testcontainers.spannerbox import SpannerboxContainer

    with SpannerboxContainer() as container:
        for env_name, env_value in env_mapping.items():
            assert container.env[env_name] == env_value


@pytest.mark.parametrize("env_mapping", [
    {
        "SPANNER_PROJECT_ID": "custom-project",
        "SPANNER_INSTANCE_ID": "custom-instance",
        "SPANNER_DATABASE_ID": "custom-database",
    },
])
def test_docker_run_spannerbox_custom_env(env_mapping):
    from testcontainers.spannerbox import SpannerboxContainer

    spannerbox_container = SpannerboxContainer(
        project_id=env_mapping["SPANNER_PROJECT_ID"],
        instance_id=env_mapping["SPANNER_INSTANCE_ID"],
        database_id=env_mapping["SPANNER_DATABASE_ID"],
    )
    with spannerbox_container as container:
        for env_name, env_value in env_mapping.items():
            assert container.env[env_name] == env_value
