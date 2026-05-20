# Guía de Semantic Kernel para Agentic System

## Introducción

Semantic Kernel es un framework ligero que permite integrar modelos de lenguaje (LLMs) con código tradicional, facilitando la creación de sistemas agentes autónomos.

## Conceptos Clave

### 1. Kernel
El kernel es el contenedor central que orquesta la ejecución de prompts, plugins y funciones.

```python
from semantic_kernel import Kernel

kernel = Kernel()
```

### 2. Plugins (Skills)
Son funciones que el agente puede ejecutar. Se dividen en:

- **Native Skills**: Funciones Python regulares
- **Semantic Skills**: Prompts semánticos que interactúan con LLMs

```python
from semantic_kernel.functions import kernel_function

class CalculatorPlugin:
    @kernel_function
    def add(self, a: int, b: int) -> int:
        return a + b
```

### 3. Prompts Semánticos
Son plantillas de prompts parametrizadas que se ejecutan con diferentes contextos.

```
{{$input}}
Responde en español: {{$language}}
Tono: {{$tone}}
```

### 4. Planificador
Orquesta la ejecución de múltiples pasos para lograr objetivos.

```python
from semantic_kernel.planning import SequentialPlanner

planner = SequentialPlanner()
plan = await planner.create_plan(goal)
result = await kernel.run_async(plan)
```

## Arquitectura para Agentic System

```
┌─────────────────────────────────────┐
│         Usuario / Cliente           │
└────────────────┬────────────────────┘
                 │
         ┌───────▼────────┐
         │  Agent Loop    │
         └────┬───────┬───┘
              │       │
        ┌─────▼─┐  ┌──▼──────┐
        │Kernel │  │ Memory  │
        └─┬───┬─┘  └────┬────┘
          │   │         │
    ┌─────▼───▼─────────▼────────┐
    │    Plugins & Skills         │
    │  ├─ Native Skills           │
    │  └─ Semantic Skills         │
    └─────────┬───────────────────┘
              │
       ┌──────▼──────┐
       │ LLM Service │
       │  (OpenAI)   │
       └─────────────┘
```

## Estructura de un Agente Básico

### 1. Inicializar Kernel

```python
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = Kernel()
kernel.add_chat_service(
    "gpt-4",
    OpenAIChatCompletion(
        model_id="gpt-4",
        api_key="sk-..."
    )
)
```

### 2. Crear Plugins

```python
from semantic_kernel.functions import kernel_function

class SearchPlugin:
    @kernel_function
    def search_web(self, query: str) -> str:
        # Implementar búsqueda
        return results
```

### 3. Registrar Plugins

```python
kernel.import_plugin(SearchPlugin(), "search")
```

### 4. Definir Prompts Semánticos

```python
from semantic_kernel.prompt_template import PromptTemplate

analysis_prompt = PromptTemplate(
    "Analiza el siguiente texto: {{$input}}\nProvee: {{$analysis_type}}"
)
kernel.create_semantic_function(
    "analyzer",
    analysis_prompt,
    "gpt-4"
)
```

### 5. Ejecutar Agente

```python
from semantic_kernel.planning import SequentialPlanner

async def run_agent():
    planner = SequentialPlanner()
    goal = "Encuentra información sobre Python y analízala"
    
    plan = await planner.create_plan(goal, kernel)
    result = await kernel.run_async(plan)
    
    return result
```

## Mejores Prácticas

### 1. Gestión de Memoria
Implementa memoria de corto y largo plazo:

```python
class AgentMemory:
    def __init__(self):
        self.short_term = []  # Última 5-10 interacciones
        self.long_term = {}   # Hechos persistentes
    
    def add_interaction(self, query, response):
        self.short_term.append((query, response))
```

### 2. Validación de Entrada
Siempre valida prompts antes de ejecutarlos:

```python
def validate_input(user_input: str) -> bool:
    return len(user_input) > 0 and len(user_input) < 5000
```

### 3. Manejo de Errores
Implementa reintentos y fallbacks:

```python
async def execute_with_fallback(kernel, goal):
    try:
        return await kernel.run_async(goal)
    except Exception as e:
        logger.error(f"Error: {e}")
        return "No pude completar la tarea. Intenta de nuevo."
```

### 4. Logging y Monitoreo
Registra todas las acciones del agente:

```python
import logging

logger = logging.getLogger("agent")
logger.info(f"Goal: {goal}")
logger.info(f"Plugins used: {plugins}")
logger.info(f"Result: {result}")
```

## Patrones de Diseño Agente

### Patrón 1: Reflexión
El agente evalúa sus propias respuestas:

```python
async def agent_with_reflection(kernel, query):
    # Genera respuesta
    response = await kernel.run_async(query)
    
    # Reflexiona sobre la respuesta
    reflection_goal = f"¿Es correcta esta respuesta? {response}"
    validation = await kernel.run_async(reflection_goal)
    
    return response, validation
```

### Patrón 2: Multi-Paso
El agente divide tareas complejas:

```python
async def multi_step_agent(kernel, complex_goal):
    planner = SequentialPlanner()
    plan = await planner.create_plan(complex_goal, kernel)
    
    for step in plan.steps:
        result = await kernel.run_async(step)
        logger.info(f"Paso: {step.description} -> {result}")
    
    return plan.result
```

### Patrón 3: Razonamiento COT (Chain of Thought)
Instrucciones explícitas para razonamiento paso a paso:

```python
cot_prompt = """
Resuelve el siguiente problema paso a paso:
1. Identifica qué se pide
2. Descompón el problema
3. Resuelve cada parte
4. Valida la solución completa

Problema: {{$input}}
"""
```

## Recursos Adicionales

- [SDK de Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Documentación oficial](https://learn.microsoft.com/semantic-kernel/)
- [Ejemplos en GitHub](https://github.com/microsoft/semantic-kernel/tree/main/samples)
- [Blog de Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/)

## Próximos Pasos

1. Implementa un agente básico de conversación
2. Integra búsqueda web como skill
3. Añade persistencia de memoria
4. Implementa planificación multi-paso
5. Despliega en producción con Docker
