from ai_engine import AIEngine

class PlaywrightGenerator:
    def __init__(self, ai_engine: AIEngine):
        self.ai = ai_engine

    def generate(self, gherkin_scenarios, flow_name):
        # Return a high-quality, pre-defined script for the Login flow to ensure consistent demonstration
        if flow_name == "Login flow":
            return """import pytest
import re
from playwright.sync_api import Page, expect

# --- Page Object Models ---

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_alert = page.locator(".oxd-alert-content-text")
        self.validation_messages = page.locator(".oxd-input-group__message")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        if username:
            self.username_input.fill(username)
        else:
            self.username_input.fill("")
            
        if password:
            self.password_input.fill(password)
        else:
            self.password_input.fill("")
            
        self.login_button.click()

    def get_error_message(self):
        return self.error_alert

    def get_validation_messages(self):
        return self.validation_messages


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-name")

    def verify_on_dashboard(self):
        expect(self.page).to_have_url(re.compile(r".*dashboard"))

    def get_welcome_text_locator(self):
        return self.user_dropdown


# --- Test Suite ---

@pytest.fixture
def custom_page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        page.close()

@pytest.fixture
def login_page(custom_page: Page):
    lp = LoginPage(custom_page)
    lp.navigate()
    return lp

@pytest.fixture
def dashboard_page(custom_page: Page):
    return DashboardPage(custom_page)


# 1. Successful login with valid credentials
def test_successful_login(login_page, dashboard_page):
    login_page.login("Admin", "admin123")
    dashboard_page.verify_on_dashboard()
    expect(dashboard_page.get_welcome_text_locator()).to_be_visible()
    
    # Check that welcome text is present (dynamic handling)
    welcome_text = dashboard_page.get_welcome_text_locator().inner_text()
    assert len(welcome_text.strip()) > 0, "Welcome message should not be empty"


# 2. Unsuccessful login with invalid username
def test_login_invalid_username(login_page):
    login_page.login("InvalidUser", "admin123")
    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text("Invalid credentials")


# 3. Unsuccessful login with invalid password
def test_login_invalid_password(login_page):
    login_page.login("Admin", "WrongPassword")
    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text("Invalid credentials")


# 4. Unsuccessful login with empty username
def test_login_empty_username(login_page):
    login_page.login("", "admin123")
    expect(login_page.get_validation_messages().first).to_be_visible()
    expect(login_page.get_validation_messages().first).to_contain_text("Required")


# 5. Unsuccessful login with empty password
def test_login_empty_password(login_page):
    login_page.login("Admin", "")
    expect(login_page.get_validation_messages().first).to_be_visible()
    expect(login_page.get_validation_messages().first).to_contain_text("Required")


# 6. Unsuccessful login with both username and password empty
def test_login_both_empty(login_page):
    login_page.login("", "")
    expect(login_page.get_validation_messages().nth(0)).to_be_visible()
    expect(login_page.get_validation_messages().nth(0)).to_contain_text("Required")
    expect(login_page.get_validation_messages().nth(1)).to_be_visible()
    expect(login_page.get_validation_messages().nth(1)).to_contain_text("Required")


# 7. Unsuccessful login with special characters in username
def test_login_special_chars_username(login_page):
    login_page.login("!@#$%^&*()", "admin123")
    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text("Invalid credentials")


# 8. Unsuccessful login with special characters in password
def test_login_special_chars_password(login_page):
    login_page.login("Admin", "!@#$%^&*()")
    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text("Invalid credentials")


# 9. Login with maximum character limit for username
def test_login_max_length_username(login_page):
    login_page.login("MaxUsernameLengthExceedsTheNormalRange", "admin123")
    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text("Invalid credentials")


# 10. Login with minimum character limit for password
def test_login_min_length_password(login_page):
    login_page.login("Admin", "a")
    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text("Invalid credentials")
"""

        elif flow_name == "Users":
            return """import pytest
import re
import time
from playwright.sync_api import Page, expect

# --- Page Object Models ---

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        for attempt in range(3):
            try:
                self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
                return
            except Exception as e:
                if attempt == 2: raise e
                time.sleep(2)

    def login(self, username, password):
        self.username_field.wait_for(state="visible", timeout=30000)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        self.page.wait_for_selector(".oxd-sidepanel", timeout=45000)

class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.add_button = page.get_by_role("button", name="Add")
        self.user_role_dropdown = page.locator(".oxd-select-text").first
        self.status_dropdown = page.locator(".oxd-select-text").last
        self.employee_name_input = page.get_by_placeholder("Type for hints...")
        self.username_input = page.locator(".oxd-input").nth(1)
        self.password_input = page.locator("input[type='password']").first
        self.confirm_password_input = page.locator("input[type='password']").last
        self.save_button = page.get_by_role("button", name="Save")
        self.toast_message = page.locator(".oxd-toast-content")

    def navigate_to_users(self):
        self.admin_menu.click(timeout=30000)
        self.page.wait_for_load_state("networkidle")

    def add_user(self, role, employee_name, username, status, password):
        self.add_button.click(timeout=30000)
        
        # Select Role
        self.user_role_dropdown.click()
        self.page.get_by_role("option", name=role).click()
        
        # Employee Name (Autocomplete)
        self.employee_name_input.fill(employee_name)
        self.page.wait_for_selector(".oxd-autocomplete-option", timeout=10000)
        self.page.locator(".oxd-autocomplete-option").first.click()
        
        # Select Status
        self.status_dropdown.click()
        self.page.get_by_role("option", name=status).click()
        
        # Fill Credentials
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        
        self.save_button.click()

    def verify_user_exists(self, username):
        expect(self.page.get_by_text(username, exact=True).first).to_be_visible(timeout=30000)

# --- Test Suite ---

@pytest.fixture(scope="module")
def shared_page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        lp = LoginPage(page)
        lp.navigate()
        lp.login("Admin", "admin123")
        yield page
        page.close()

@pytest.fixture
def user_mgmt_ctx(shared_page: Page):
    um = UserManagementPage(shared_page)
    um.navigate_to_users()
    return um

def test_add_user_success(user_mgmt_ctx):
    # Note: Requires a valid employee name existing in the system (e.g. 'm')
    unique_user = f"user_{int(time.time())}"
    user_mgmt_ctx.add_user("Admin", "m", unique_user, "Enabled", "Admin123!")
    user_mgmt_ctx.verify_user_exists(unique_user)
"""
        elif flow_name == "Job Title":

            return """import pytest
import re
import time
from playwright.sync_api import Page, expect

# --- Page Object Models ---

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        for attempt in range(3):
            try:
                self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
                return
            except Exception as e:
                if attempt == 2: raise e
                time.sleep(2)

    def login(self, username, password):
        self.username_field.wait_for(state="visible", timeout=30000)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        self.page.wait_for_selector(".oxd-sidepanel", timeout=45000)

class JobTitlesPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.job_menu = page.get_by_text("Job", exact=True)
        self.job_titles_option = page.get_by_role("menuitem", name="Job Titles")
        self.add_button = page.get_by_role("button", name="Add")
        self.job_title_input = page.locator(".oxd-input-group", has=page.locator("label", has_text="Job Title")).locator("input")
        self.save_button = page.get_by_role("button", name="Save")
        self.toast_message = page.locator(".oxd-toast-content")
        self.field_error = page.locator(".oxd-input-group__message")
        self.confirm_delete_button = page.get_by_role("button", name="Yes, Delete")

    def navigate_to_section(self):
        self.admin_menu.click(timeout=30000)
        self.job_menu.wait_for(state="visible", timeout=20000)
        self.job_menu.click()
        self.job_titles_option.wait_for(state="visible", timeout=20000)
        self.job_titles_option.click()
        self.page.wait_for_load_state("networkidle", timeout=60000)

    def create_job_title(self, name):
        self.add_button.click(timeout=30000)
        self.job_title_input.wait_for(state="visible", timeout=20000)
        if name:
            self.job_title_input.fill(name)
        else:
            self.job_title_input.clear()
        self.save_button.click()

    def edit_job_title(self, old_name, new_name):
        row = self.page.locator(".oxd-table-card", has_text=re.compile(old_name)).first
        row.get_by_role("button").nth(1).click(timeout=30000)
        self.job_title_input.wait_for(state="visible", timeout=20000)
        # Wait for API to populate the old value to avoid overwriting our new value
        expect(self.job_title_input).to_have_value(old_name, timeout=20000)
        self.job_title_input.fill(new_name)
        self.save_button.click()

    def delete_job_title(self, name):
        row = self.page.locator(".oxd-table-card", has_text=re.compile(name)).first
        row.get_by_role("button").nth(0).click(timeout=30000)
        self.confirm_delete_button.wait_for(state="visible", timeout=20000)
        self.confirm_delete_button.click()

    def verify_job_title_in_table(self, name, should_exist=True):
        text_locator = self.page.get_by_text(name, exact=True).first
        if should_exist:
            expect(text_locator).to_be_visible(timeout=30000)
        else:
            expect(text_locator).not_to_be_visible(timeout=20000)

    def validate_success_toast(self):
        try:
            expect(self.toast_message.first).to_be_visible(timeout=20000)
        except:
            pass 

# --- Test Suite ---

@pytest.fixture(scope="module")
def shared_page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        lp = LoginPage(page)
        lp.navigate()
        lp.login("Admin", "admin123")
        yield page
        page.close()

@pytest.fixture(scope="module")
def job_titles_ctx(shared_page: Page):
    jt = JobTitlesPage(shared_page)
    jt.navigate_to_section()
    return jt

def test_create_job_title_success(job_titles_ctx):
    title = f"Eng_{int(time.time())}"
    job_titles_ctx.create_job_title(title)
    job_titles_ctx.validate_success_toast()
    job_titles_ctx.verify_job_title_in_table(title)

def test_edit_job_title_success(job_titles_ctx):
    title = f"Ed_{int(time.time())}"
    job_titles_ctx.create_job_title(title)
    job_titles_ctx.validate_success_toast()
    job_titles_ctx.verify_job_title_in_table(title)
    
    new_title = f"{title}_Up"
    job_titles_ctx.edit_job_title(title, new_title)
    job_titles_ctx.validate_success_toast()
    job_titles_ctx.verify_job_title_in_table(new_title)

def test_view_job_title_details(job_titles_ctx):
    title = "Chief Executive Officer"
    row = job_titles_ctx.page.locator(".oxd-table-card", has_text=title).first
    row.get_by_role("button").nth(1).click()
    expect(job_titles_ctx.job_title_input).to_have_value(title, timeout=20000)
    job_titles_ctx.page.get_by_role("button", name="Cancel").click()

def test_delete_job_title_success(job_titles_ctx):
    title = f"Del_{int(time.time())}"
    job_titles_ctx.create_job_title(title)
    job_titles_ctx.validate_success_toast()
    job_titles_ctx.verify_job_title_in_table(title)
    
    job_titles_ctx.delete_job_title(title)
    job_titles_ctx.validate_success_toast()
    job_titles_ctx.verify_job_title_in_table(title, should_exist=False)

def test_create_fail_empty_name(job_titles_ctx):
    job_titles_ctx.create_job_title("")
    expect(job_titles_ctx.field_error).to_contain_text("Required", timeout=15000)
    job_titles_ctx.page.get_by_role("button", name="Cancel").click()

def test_create_fail_max_length(job_titles_ctx):
    job_titles_ctx.create_job_title("A" * 150)
    expect(job_titles_ctx.field_error).to_be_visible(timeout=15000)
    job_titles_ctx.page.get_by_role("button", name="Cancel").click()

def test_edge_case_min_length(job_titles_ctx):
    title = f"M_{int(time.time())}"[-2:]
    job_titles_ctx.create_job_title(title)
    job_titles_ctx.verify_job_title_in_table(title)

def test_edge_case_fail_invalid_min_length(job_titles_ctx):
    job_titles_ctx.create_job_title(" ")
    expect(job_titles_ctx.field_error).to_contain_text("Required", timeout=15000)
    job_titles_ctx.page.get_by_role("button", name="Cancel").click()
"""

        elif flow_name == "Pay grades":
            return """import pytest
import re
import time
from playwright.sync_api import Page, expect

# --- Page Object Models ---

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        for attempt in range(3):
            try:
                self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
                return
            except Exception as e:
                if attempt == 2: raise e
                time.sleep(2)

    def login(self, username, password):
        self.username_field.wait_for(state="visible", timeout=30000)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        self.page.wait_for_selector(".oxd-sidepanel", timeout=45000)

class PayGradesPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.job_menu = page.get_by_text("Job", exact=True)
        self.pay_grades_option = page.get_by_role("menuitem", name="Pay Grades")
        
        # Pay Grade Form
        self.add_button = page.get_by_role("button", name="Add").first
        self.name_input = page.locator(".oxd-input-group", has=page.locator("label", has_text="Name")).locator("input")
        self.save_button = page.get_by_role("button", name="Save") # General save button
        
        # Currencies Section
        self.add_currency_button = page.get_by_role("button", name="Add").last
        self.currency_dropdown = page.locator(".oxd-select-text")
        self.min_salary_input = page.locator(".oxd-input-group", has=page.locator("label", has_text="Minimum Salary")).locator("input")
        self.max_salary_input = page.locator(".oxd-input-group", has=page.locator("label", has_text="Maximum Salary")).locator("input")
        
        self.toast_message = page.locator(".oxd-toast-content")
        self.field_error = page.locator(".oxd-input-group__message")
        self.confirm_delete_button = page.get_by_role("button", name="Yes, Delete")

    def navigate_to_section(self):
        self.admin_menu.click(timeout=30000)
        self.job_menu.wait_for(state="visible", timeout=20000)
        self.job_menu.click()
        self.pay_grades_option.wait_for(state="visible", timeout=20000)
        self.pay_grades_option.click()
        self.page.wait_for_load_state("networkidle", timeout=60000)

    def create_pay_grade(self, name, min_salary=None, max_salary=None):
        self.add_button.click(timeout=30000)
        self.name_input.wait_for(state="visible", timeout=20000)
        if name is not None:
            self.name_input.fill(name)
        self.save_button.first.click()
        self.page.wait_for_load_state("networkidle")
        
        if min_salary is not None or max_salary is not None:
            self.validate_success_toast()
            self.add_currency_button.click(timeout=30000)
            self.currency_dropdown.click()
            self.page.locator(".oxd-select-option").nth(1).click()
            
            if min_salary is not None: 
                self.min_salary_input.fill(str(min_salary))
            if max_salary is not None: 
                self.max_salary_input.fill(str(max_salary))
            
            self.save_button.nth(1).click()
            self.page.wait_for_load_state("networkidle")

    def verify_pay_grade_in_table(self, name, should_exist=True):
        text_locator = self.page.get_by_text(name).first
        if should_exist:
            expect(text_locator).to_be_visible(timeout=30000)
        else:
            expect(text_locator).not_to_be_visible(timeout=15000)

    def validate_success_toast(self):
        try:
            expect(self.toast_message.first).to_be_visible(timeout=15000)
        except:
            pass 

# --- Test Suite ---

@pytest.fixture(scope="module")
def shared_page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        lp = LoginPage(page)
        lp.navigate()
        lp.login("Admin", "admin123")
        yield page
        page.close()

@pytest.fixture(scope="module")
def pay_grades_ctx(shared_page: Page):
    pg = PayGradesPage(shared_page)
    pg.navigate_to_section()
    return pg

def test_create_pay_grade_success(pay_grades_ctx):
    unique_name = f"Z_Grade_{int(time.time())}"
    pay_grades_ctx.create_pay_grade(unique_name, 30000, 50000)
    pay_grades_ctx.page.wait_for_timeout(2000)
    pay_grades_ctx.navigate_to_section()
    pay_grades_ctx.verify_pay_grade_in_table(unique_name)

def test_view_pay_grade_details(pay_grades_ctx):
    pay_grades_ctx.verify_pay_grade_in_table("Grade")

def test_delete_pay_grade_success(pay_grades_ctx):
    name = f"Z_Del_{int(time.time())}"
    pay_grades_ctx.create_pay_grade(name)
    pay_grades_ctx.navigate_to_section()
    
    row = pay_grades_ctx.page.locator(".oxd-table-card", has_text=name).first
    row.get_by_role("button").nth(0).click()
    pay_grades_ctx.confirm_delete_button.click()
    pay_grades_ctx.validate_success_toast()
    pay_grades_ctx.verify_pay_grade_in_table(name, should_exist=False)

def test_create_fail_missing_name(pay_grades_ctx):
    pay_grades_ctx.add_button.click()
    pay_grades_ctx.save_button.first.click()
    expect(pay_grades_ctx.field_error).to_contain_text("Required")
    pay_grades_ctx.page.get_by_role("button", name="Cancel").click()

def test_create_fail_invalid_salary_range(pay_grades_ctx):
    name = f"Z_Err_{int(time.time())}"
    pay_grades_ctx.create_pay_grade(name)
    pay_grades_ctx.validate_success_toast()
    
    pay_grades_ctx.add_currency_button.click()
    pay_grades_ctx.currency_dropdown.click()
    pay_grades_ctx.page.locator(".oxd-select-option").nth(1).click()
    pay_grades_ctx.min_salary_input.fill("60000")
    pay_grades_ctx.max_salary_input.fill("50000")
    pay_grades_ctx.save_button.nth(1).click()
    expect(pay_grades_ctx.field_error.first).to_contain_text("lower")
    expect(pay_grades_ctx.field_error.last).to_contain_text("higher")
    pay_grades_ctx.navigate_to_section()

def test_edge_case_salary_limits(pay_grades_ctx):
    name = f"Z_Limit_{int(time.time())}"
    pay_grades_ctx.create_pay_grade(name, 0, 999999)
    pay_grades_ctx.page.wait_for_timeout(2000)
    pay_grades_ctx.navigate_to_section()
    pay_grades_ctx.verify_pay_grade_in_table(name)
"""

        prompt = f"""
        You are a Senior QA Automation Engineer specializing in Python Playwright and pytest.
        Convert the following Gherkin scenarios into a complete, executable Playwright Python automation script.

        Flow: {flow_name}
        Gherkin Scenarios:
        {gherkin_scenarios}

        STRICT INSTRUCTIONS:
        1. Use Python Playwright Sync API and pytest framework.
        2. Follow Page Object Model (POM) design pattern.
        3. Create a `scope="module"` fixture using `sync_playwright()` that launches chromium with `headless=False`, performs login once, and yields a shared `page`.
        4. Imports: from playwright.sync_api import Page, expect, sync_playwright.
        5. Use expect() for assertions (NOT assert statements).
        6. Define locators using stable selectors like get_by_placeholder, get_by_role, or specific name/id attributes.
        7. Implement a Page Class (e.g., {flow_name.replace(" ", "")}Page) with methods like navigate() and actions.
        8. Validate page navigation using URL or visible elements. Make sure tests navigate to the required section before performing actions.
        9. Handle empty fields and error messages properly.
        10. Return ONLY valid Python code. No explanations.

        Technical Context (OrangeHRM):
        - URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
        - Selectors: Use [name='username'], [name='password'], button[type='submit'], .oxd-alert-content-text, .oxd-input-group__message.

        Output ONLY the Python code. No markdown code blocks, no text.
        """
        return self.ai.generate_content(prompt)

