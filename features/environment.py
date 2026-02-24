from playwright.sync_api import sync_playwright #Herramiento de automatiizacion de navegadores

def before_all(context): # Encender todo
    context.playwright = sync_playwright().start() # Inicia el Playwright
    context.browser = context.playwright.chromium.launch( # Abre el Chrome
        headless=False, # Vemos el navegador abrirse. Si fuera True la accion pasaria en segundo plano
        slow_mo=800 # Relentizamos para que podamos ver lo que esta ocurriendo
    )
    context.context = context.browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    context.page = context.context.new_page() # Crea un contexto de navegador

    context.page = context.context.new_page()
    context.page.goto("http://localhost:5173/login")

def after_all(context):
    context.browser.close() # Cerramos navegador
    context.playwright.stop() # Detenemos el playwright