# Email Test Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a manually triggered GitHub Actions workflow that sends one SMTP test email without running stock analysis.

**Architecture:** The workflow checks out the repository, installs the existing Python dependencies, loads email settings through `get_config()`, and calls the existing `EmailSender`. A failed send exits non-zero so the Actions result reflects the SMTP outcome.

**Tech Stack:** GitHub Actions, Python 3.11, pytest, existing `EmailSender`

---

### Task 1: Add static workflow coverage

**Files:**
- Create: `tests/test_email_workflow.py`

- [ ] Parse `.github/workflows/test_email.yml`.
- [ ] Assert it is manually triggered and maps only the required email credentials.
- [ ] Assert the workflow calls `EmailSender.send_to_email()` and does not run `main.py`.

### Task 2: Add the email test workflow

**Files:**
- Create: `.github/workflows/test_email.yml`

- [ ] Add a `workflow_dispatch` trigger.
- [ ] Install the repository dependencies on Python 3.11.
- [ ] Map `EMAIL_SENDER`, `EMAIL_PASSWORD`, and `EMAIL_RECEIVERS`.
- [ ] Send a clearly labeled test message.
- [ ] Exit with status 1 when SMTP sending fails.

### Task 3: Verify and deploy

- [ ] Run `pytest tests/test_email_workflow.py -q`.
- [ ] Commit and push the workflow to `main`.
- [ ] Trigger `test_email.yml`.
- [ ] Inspect the workflow log for the SMTP result.
