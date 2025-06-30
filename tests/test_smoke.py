import pytest

@pytest.mark.fast
@pytest.mark.smoke
def test_import():
    import template_project_name

    print(template_project_name)
