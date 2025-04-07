workspace "Name" "Description" {

    model {
        user = person "Usuario" "Un usuario que ejecuta la aplicación CLI para procesar transacciones bancarias."

        processor = softwareSystem "Procesador de Transacciones Bancarias" "Una herramienta CLI que procesa archivos CSV de transacciones bancarias y genera reportes." {
            domain = container "Dominio" "Define las entidades y reglas esenciales del negocio."
            application = container "Aplicación" "Implementa los procesos y cálculos para analizar transacciones."
            infrastructure = container "Infraestructura" "Proporciona funcionalidad para leer archivos CSV."
            presentation = container "Presentación" "Gestiona la visualización de reportes y la interacción con el usuario."
        }

        user -> presentation "Interacciona a través de la interfaz"
        presentation -> infrastructure "Solicita lógica de negocio"
        presentation -> application "Solicita acceso a datos"
        infrastructure -> domain "Opera sobre las entidades definidas"
        application -> domain "Transforma datos en entidades"
    }

    views {
        systemContext processor "Diagram1" {
            include *
            autolayout lr
        }

        container processor "Diagram2" {
            include *
            autolayout lr
        }

        styles {
            element "Software System" {
                width 500
            }
            element "Boundary:SoftwareSystem" {
                fontSize 36
            }
        }

        theme default
    }
}