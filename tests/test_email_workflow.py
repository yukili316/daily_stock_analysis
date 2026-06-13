# -*- coding: utf-8 -*-
"""Static checks for the standalone email test workflow."""

from pathlib import Path

import yaml


ROOT_DIR = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = ROOT_DIR / ".github/workflows/test_email.yml"


def test_email_workflow_is_manual_and_isolated() -> None:
    raw = WORKFLOW_PATH.read_text(encoding="utf-8")
    workflow = yaml.safe_load(raw)

    triggers = workflow.get("on", workflow.get(True))
    assert "workflow_dispatch" in triggers

    steps = workflow["jobs"]["test-email"]["steps"]
    send_step = next(step for step in steps if step.get("name") == "发送测试邮件")
    assert send_step["env"] == {
        "EMAIL_SENDER": "${{ secrets.EMAIL_SENDER }}",
        "EMAIL_PASSWORD": "${{ secrets.EMAIL_PASSWORD }}",
        "EMAIL_RECEIVERS": "${{ secrets.EMAIL_RECEIVERS }}",
    }

    script = send_step["run"]
    assert "config = get_config()" in script
    assert "EmailSender(config)" in script
    assert "send_to_email(" in script
    assert 'value.encode("ascii")' in script
    assert "main.py" not in raw
    assert "STOCK_LIST" not in raw
