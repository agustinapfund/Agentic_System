# -*- coding: utf-8 -*-
"""
Ejemplo básico de un Agente Conversacional con Semantic Kernel
Demuestra la inicialización, creación de plugins y ejecución del agente.
"""

import asyncio
from typing import Optional
from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion


class ConversationalAgent:
    """Agente conversacional básico con Semantic Kernel"""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        """
        Inicializa el agente
        
        Args:
            api_key: Clave API de OpenAI
            model: Modelo a utilizar (gpt-4, gpt-3.5-turbo, etc.)
        """
        self.kernel = Kernel()
        self.model = model
        
        # Configurar servicio de LLM
        self.kernel.add_chat_service(
            model,
            OpenAIChatCompletion(
                model_id=model,
                api_key=api_key
            )
        )
        
        # Memoria del agente
        self.conversation_history = []
        self.agent_memory = {}
    
    def _build_conversation_context(self) -> str:
        """Construye el contexto de conversación"""
        context = "Historial de conversación:\n"
        for msg in self.conversation_history[-5:]:  # Últimos 5 mensajes
            context += f"- {msg['role']}: {msg['content']}\n"
        return context
    
    async def process_user_input(self, user_input: str) -> str:
        """
        Procesa entrada del usuario y genera respuesta
        
        Args:
            user_input: Entrada del usuario
            
        Returns:
            Respuesta del agente
        """
        # Agregar entrada al historial
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Construir prompt con contexto
        context = self._build_conversation_context()
        
        prompt = f"""
Tu eres un asistente inteligente. Responde en español.

{context}

Usuario: {user_input}
Asistente:
"""
        
        # Ejecutar con Semantic Kernel
        try:
            response = await self.kernel.run_async(
                self.model,
                input=prompt
            )
            
            # Agregar respuesta al historial
            self.conversation_history.append({
                "role": "assistant",
                "content": str(response)
            })
            
            return str(response)
        except Exception as e:
            error_msg = f"Error al procesar: {str(e)}"
            return error_msg
    
    async def run_conversation_loop(self):
        """Ejecuta un loop de conversación interactiva"""
        print("Agente Conversacional Iniciado")
        print("Escribe 'salir' para terminar\n")
        
        while True:
            try:
                user_input = input("Tú: ").strip()
                
                if user_input.lower() == "salir":
                    print("Agente: ¡Hasta luego!")
                    break
                
                if not user_input:
                    continue
                
                response = await self.process_user_input(user_input)
                print(f"Agente: {response}\n")
                
            except KeyboardInterrupt:
                print("\nAgente: Terminando...")
                break
            except Exception as e:
                print(f"Error: {str(e)}")


class AdvancedAgent(ConversationalAgent):
    """Agente avanzado con plugins personalizados"""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        super().__init__(api_key, model)
        self._register_plugins()
    
    def _register_plugins(self):
        """Registra plugins personalizados"""
        
        class MathPlugin:
            @kernel_function
            def calculate(self, expression: str) -> str:
                """Ejecuta cálculos matemáticos"""
                try:
                    result = eval(expression)
                    return f"Resultado: {result}"
                except Exception as e:
                    return f"Error en cálculo: {str(e)}"
        
        class InfoPlugin:
            @kernel_function
            def get_info(self, topic: str) -> str:
                """Proporciona información sobre temas"""
                info_db = {
                    "python": "Python es un lenguaje de programación versátil",
                    "semantic kernel": "SK es un framework de IA de Microsoft",
                    "agentes": "Los agentes IA son sistemas autónomos de toma de decisiones"
                }
                return info_db.get(topic.lower(), "Tema no encontrado")
        
        # Importar plugins
        self.kernel.import_plugin(MathPlugin(), "math")
        self.kernel.import_plugin(InfoPlugin(), "info")


async def main():
    """Función principal"""
    import os
    
    # Obtener API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: Configure la variable OPENAI_API_KEY")
        return
    
    # Crear y ejecutar agente
    agent = ConversationalAgent(api_key)
    await agent.run_conversation_loop()


if __name__ == "__main__":
    asyncio.run(main())
