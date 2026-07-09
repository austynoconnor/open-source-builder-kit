from open_source_builder_kit.validation import validate_example_manifests


def test_validate_example_manifests_scores_all_examples() -> None:
    results = validate_example_manifests()

    assert len(results) == 2
    assert {result.project_name for result in results} == {
        "Civic Data Commons",
        "Learning Lab Toolkit",
    }
    assert all(result.score > 0 for result in results)
