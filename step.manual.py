from sinara.step import Step
from sinara.step import StepSafeguard as sg
from sinara.step import StepReport as sr

sg.git_reset()

try:
    step = Step(run_params_file_globs="params/step_params.json",
           env_name="user")
    for notebook in step.notebooks:
        notebook.run()
except Exception as e:
    step.handle_exception(e)
finally:
    sr.tag_commit_by_run()
    step.handle_exit()
