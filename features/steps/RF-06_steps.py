from behave import given, when, then
from pages.base_page import BasePage


@given("el mentor inicia sesión")
def step_login(context):
    context.base_page = BasePage(context.page)

    context.page.goto("http://localhost:5173/login")

    context.base_page.fill("//input[@name='email']", "usuario@demo.com") # Ingresamos usuario de prueba
    context.base_page.fill("//input[@name='password']", "123456") # Ingresamos contraseña del usuario de prueba
    context.base_page.click("//button[text()='Iniciar Sesión']") # Hacemos click en el boton de iniciar sesion
    context.page.wait_for_timeout(3000) # Pausa para que no se cargue todo tan tapido

@when("selecciona el módulo de 'mentoría'")
def step_ir_mentoria(context):
    context.base_page.click("//span[text()='Sesiones']") # Click en boton sesiones


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
