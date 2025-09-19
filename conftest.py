import pytest, allure
from playwright.sync_api import sync_playwright, Page
from pathlib import Path

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page and isinstance(page, Page):
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            test_name = report.nodeid.replace("::", "_")[1:]
            screenshot_path = screenshot_dir / f"{test_name}.png"

            page.screenshot(path=str(screenshot_path))
            print(f"\nСкриншот сохранен: {screenshot_path}")

            allure.attach(
                page.screenshot(full_page=True),
                name=f"screenshot_{test_name}",
                attachment_type=allure.attachment_type.PNG
            )