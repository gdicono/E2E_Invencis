Feature: Solicitud de sesión

  Scenario: El usuario solicita sesión tipo Shadow correctamente
    Given el usuario inicia sesión
    When selecciona tipo de sesión 'Shadow'
    And selecciona una fecha disponible
    And selecciona una hora disponible
    And confirma la solicitud
    Then debería ver un mensaje de confirmación