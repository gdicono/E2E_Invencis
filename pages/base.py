class BasePage:

    def __init__(self, page): # Constructor
        self.page = page

    def click(self, selector): # Metodo click que recibe un selecto (Xpath)
        self.page.click(selector) #Llama al metodo de click de playwright para que haga click en el item que coincide con el selector

    def fill(self, selector, text): # Metodo en el que queremos ingresar un input a travez del selector
        self.page.fill(selector, text) # En el selector ponemoe el text que queremos