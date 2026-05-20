# Agentic System

🚀 **Estado:** En Incubación - Fase de Desarrollo  
🔬 **Tipo:** Proyecto Experimental  
⚙️ **Tecnología Principal:** Semantic Kernel + Agentic Patterns

Agentic System es un proyecto que integra un enfoque agente para la automatización inteligente de chatbots, con aplicación avanzada de Semantic Kernel para orquestación de tareas y razonamiento semántico.

## Qué es
Este repositorio propone un sistema agente que coordina tareas, gestiona flujo de conversación y utiliza capacidades de razonamiento y memoria para mejorar la interacción con usuarios.

## Aplicación de Semantic Kernel
Semantic Kernel se usa como base para:

- Modelar agentes con comportamientos dinámicos.
- Ejecutar planes y orquestar acciones con objetivo.
- Incorporar capacidades de lenguaje natural para interpretar intenciones.
- Conectar prompts, habilidades y datos semánticos en un flujo coherente.

## Recursos y Documentación

Para desarrollar sistemas agentes con Semantic Kernel, consulta:

- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/) - Documentación oficial de Microsoft
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel) - Código fuente y ejemplos
- [Agentic Design Patterns](https://learn.microsoft.com/en-us/semantic-kernel/concepts/agents) - Patrones de diseño agente
- [AI Agents Handbook](https://www.deeplearning.ai/short-courses/) - Cursos especializados en agentes IA
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Guía completa de ingeniería de prompts

## Características principales

- Arquitectura agente-centrista para chatbots avanzados.
- Soporte para tareas múltiples y seguimiento de estado.
- Capacidad para utilizar memoria y contexto en conversaciones.
- Enfoque modular para integrar nuevas habilidades y servicios.

## Cómo comenzar
1. Clonar el repositorio.
2. Revisar la estructura de código y la configuración existente.
3. Adaptar la implementación a tu fuente de datos y modelo preferido.

## Estructura del Proyecto

```
Agentic_System/
├── src/
│   ├── agents/              # Implementación de agentes inteligentes
│   │   ├── base_agent.py
│   │   ├── conversational_agent.py
│   │   └── task_agent.py
│   ├── kernels/             # Configuración y setup de Semantic Kernel
│   │   ├── kernel_builder.py
│   │   ├── kernel_config.py
│   │   └── kernel_manager.py
│   ├── plugins/             # Plugins y habilidades (skills)
│   │   ├── native_skills/
│   │   ├── semantic_skills/
│   │   └── plugin_registry.py
│   ├── memory/              # Gestión de memoria semántica
│   │   ├── memory_store.py
│   │   ├── short_term_memory.py
│   │   └── long_term_memory.py
│   ├── orchestration/       # Orquestación de flujos y planes
│   │   ├── planner.py
│   │   ├── executor.py
│   │   └── workflow_manager.py
│   ├── models/              # Modelos de datos y entidades
│   │   ├── agent_models.py
│   │   ├── message.py
│   │   └── context.py
│   └── services/            # Servicios auxiliares
│       ├── llm_service.py
│       ├── embedding_service.py
│       └── api_service.py
├── prompts/                 # Prompts semánticos
│   ├── system/              # Prompts de sistema
│   └── skills/              # Prompts para skills
├── config/                  # Archivos de configuración
│   ├── dev.yaml
│   ├── prod.yaml
│   └── env.example
├── tests/                   # Suite de pruebas
│   ├── unit/
│   └── integration/
├── docs/                    # Documentación del proyecto
│   ├── architecture.md
│   ├── semantic-kernel-guide.md
│   └── agent-patterns.md
├── examples/                # Ejemplos de uso
│   ├── basic_agent.py
│   ├── chatbot_example.py
│   └── task_automation.py
├── infrastructure/          # Configuración de infraestructura
│   ├── docker/
│   └── kubernetes/
├── scripts/                 # Scripts de utilidad
│   ├── setup.sh
│   └── run.sh
└── README.md
```

### Descripción de Carpetas

| Carpeta | Propósito |
|---------|-----------|
| **src/agents** | Lógica central de agentes inteligentes con razonamiento y toma de decisiones |
| **src/kernels** | Inicialización y configuración de Semantic Kernel y servicios |
| **src/plugins** | Extensiones de funcionalidad (skills nativas y semánticas) |
| **src/memory** | Sistemas de memoria (corta y larga duración) para contexto persistente |
| **src/orchestration** | Planificación, ejecución y gestión de workflows agentes |
| **src/models** | Definiciones de datos, esquemas y estructuras del agente |
| **src/services** | Servicios de LLM, embeddings e integraciones externas |
| **prompts** | Almacen centralizado de prompts semánticos y plantillas |
| **config** | Configuración por ambiente (desarrollo, producción) |
| **tests** | Pruebas unitarias e integración con Semantic Kernel |
| **docs** | Guías, arquitectura y patrones de diseño |
| **examples** | Casos de uso demostrativos e implementaciones de referencia |
| **infrastructure** | Dockerización y configuración de deployment |
| **scripts** | Automatización de setup e ejecución |

## Cómo comenzar

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/agustinapfund/Agentic_System.git
   cd Agentic_System
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp config/env.example .env
   # Edita .env con tus valores (API keys, etc.)
   ```

5. **Ejecutar un ejemplo**
   ```bash
   python examples/basic_agent.py
   ```

### Crear tu primer Agente

```python
from src.agents.base_agent import AgenticAgent
from semantic_kernel import Kernel

# Inicializar
kernel = Kernel()
agent = AgenticAgent(kernel)

# Ejecutar
resultado = await agent.process("¿Cuál es la capital de España?")
print(resultado)
```

## Documentación Disponible

- 📖 [Guía Semantic Kernel](docs/SEMANTIC_KERNEL_GUIDE.md) - Conceptos y patrones
- 🏗️ [Arquitectura del Sistema](docs/architecture.md) - Diseño y componentes
- 💡 [Patrones Agente](docs/agent-patterns.md) - Implementación de patrones
- 🔧 [Ejemplos Prácticos](examples/) - Casos de uso listos para usar

## Uso esperado

Este proyecto puede servir como base para:

- chatbots conversacionales potentes.
- asistentes virtuales que planifican acciones.
- sistemas de automatización inteligente con memoria semántica.

## Licencia
Añade aquí la licencia correspondiente según tu proyecto.
