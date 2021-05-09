from hooks.post_gen_project import setup_pre_commit


def test_setup_pre_commit(mocker):
    subprocess_run = mocker.patch("subprocess.run")

    setup_pre_commit()

    assert subprocess_run.call_count == 4
    subprocess_run.assert_any_call(
        ["pre-commit", "-h"], check=True, capture_output=True
    )
    subprocess_run.assert_any_call(["pre-commit", "install"], check=True)
