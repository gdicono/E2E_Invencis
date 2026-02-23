Feature: Finalización de sesión

  Scenario: El mentor finaliza una sesión correctamente
    Given el mentor inicia sesión
    And selecciona el módulo de 'mentoría'
    When selecciona una sesión activa
    And hace clic en finalizar sesión
    Then debería ver un mensaje de sesión finalizada