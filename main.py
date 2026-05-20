#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Agentic System - Main Entry Point
Punto de entrada principal para el sistema agente con Semantic Kernel
"""

import asyncio
import logging
from pathlib import Path
from typing import Optional

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    """Función principal de ejecución"""
    logger.info("=" * 50)
    logger.info("Agentic System - Iniciando...")
    logger.info("=" * 50)
    
    try:
        # Importar ejemplo básico
        from examples.basic_agent import ConversationalAgent
        import os
        
        # Verificar API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("Error: Configure la variable OPENAI_API_KEY en el archivo .env")
            logger.info("\nPasos:")
            logger.info("1. Copia config/env.example a .env")
            logger.info("2. Añade tu clave de OpenAI en OPENAI_API_KEY")
            logger.info("3. Ejecuta nuevamente: python main.py")
            return
        
        logger.info("✓ API Key configurada correctamente")
        
        # Crear agente
        agent = ConversationalAgent(api_key)
        logger.info("✓ Agente creado exitosamente")
        
        # Ejecutar conversación
        logger.info("\nIniciando modo conversacional...")
        logger.info("-" * 50)
        await agent.run_conversation_loop()
        
    except ImportError as e:
        logger.error(f"Error de importación: {str(e)}")
        logger.info("\nSolución:")
        logger.info("Instala las dependencias: pip install -r requirements.txt")
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        raise


def show_welcome():
    """Muestra mensaje de bienvenida"""
    welcome = """
╔════════════════════════════════════════════════════════════╗
║         🤖 AGENTIC SYSTEM - Sistema Agente IA 🤖          ║
║          Powered by Semantic Kernel (Microsoft)           ║
╚════════════════════════════════════════════════════════════╝

📚 Recursos:
   • Documentación: docs/SEMANTIC_KERNEL_GUIDE.md
   • Ejemplos: examples/
   • Configuración: .env (copia desde config/env.example)

🚀 Quick Start:
   1. Configura tu API key en .env
   2. Ejecuta: python main.py
   3. Interactúa con el agente

💡 Tips:
   • Escribe preguntas en español
   • Escribe 'salir' para terminar
   • Revisa los logs para más información

════════════════════════════════════════════════════════════
    """
    print(welcome)


if __name__ == "__main__":
    show_welcome()
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n¡Sistema detenido!")
    except Exception as e:
        logger.error(f"Error fatal: {str(e)}")
        exit(1)
