from behave import given, when, then
from pages.base_page import BasePage


@given("el mentor inicia sesión")
def step_login(context):
    context.base_page = BasePage(context.page)

    context.page.goto("http://localhost:5173")

    context.base_page.fill()
    context.base_page.fill()
    context.base_page.click()


@when("selecciona el módulo de 'mentoría'")
def step_ir_mentoria(context):
    context.base_page.click()


@when("selecciona una sesión activa")
def step_seleccionar_sesion(context):
    context.base_page.click()


@when("hace clic en finalizar sesión")
def step_finalizar(context):
    context.base_page.click()


@then("debería ver un mensaje de sesión finalizada")
def step_validacion(context):
    mensaje = context.page.text_content()
    assert mensaje is not None
