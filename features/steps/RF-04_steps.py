from behave import given, when, then
from pages.base_page import BasePage

@given ("el usuario inicia sesión")
def step_login(context):
    context.base_page= BasePage(context)
    context.page.goto ("http://localhost:5173")

    context.base_page.fill()

    context.base_page.fill()

    context.base_page.click()

@when("selecciona tipo de sesión 'Shadow'")
def step_tipo_shadow(context):
    context.base_page.click()

@when("selecciona una fecha disponible")
def step_fecha(context):
    context.base_page.click()
    context.base_page.click()


@when("selecciona una hora disponible")
def step_hora(context):
    context.base_page.click()


@when("confirma la solicitud")
def step_confirmar(context):
    context.base_page.click()


@then("debería ver un mensaje de confirmación")
def step_validacion(context):
    mensaje = context.page.text_content()
    assert mensaje is not None

