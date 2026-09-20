import re
import sys
import os
from pathlib import Path
from typing import List, Dict, Optional
import argparse
from bs4 import BeautifulSoup
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class WorkflowExtractor:
    """Extractor de información de workflows desde HTML a Markdown."""
    
    def __init__(self, html_file_path: str):
        """
        Inicializa el extractor con la ruta del archivo HTML.
        
        Args:
            html_file_path: Ruta al archivo HTML a procesar
        """
        self.html_file_path = Path(html_file_path)
        self.html_content = ""
        self.workflows = []
        
    def read_html_file(self) -> bool:
        """
        Lee el contenido del archivo HTML.
        
        Returns:
            True si la lectura fue exitosa, False en caso contrario
        """
        try:
            if not self.html_file_path.exists():
                logger.error(f"El archivo no existe: {self.html_file_path}")
                return False
                
            with open(self.html_file_path, 'r', encoding='utf-8') as f:
                self.html_content = f.read()
            logger.info(f"Archivo leído exitosamente: {self.html_file_path}")
            return True
        except Exception as e:
            logger.error(f"Error al leer el archivo: {e}")
            return False
    
    def extract_with_beautifulsoup(self) -> List[Dict[str, str]]:
        """
        Extrae información usando BeautifulSoup (método recomendado).
        Elimina duplicados basándose en el nombre del archivo.
        
        Returns:
            Lista de diccionarios con la información de cada workflow (sin duplicados)
        """
        workflows = []
        seen_filenames = set()  # Para rastrear workflows ya procesados
        duplicate_count = 0
        
        soup = BeautifulSoup(self.html_content, 'html.parser')
        
        # Buscar todas las tarjetas de workflow
        cards = soup.find_all('div', class_='workflow-card')
        
        for card in cards:
            try:
                workflow = {}
                
                # Extraer link
                link_elem = card.find('a', href=True)
                workflow['link'] = link_elem['href'] if link_elem else ''
                
                # Extraer nombre del archivo (primer span dentro del link)
                filename_elem = link_elem.find('span') if link_elem else None
                workflow['filename'] = filename_elem.text.strip() if filename_elem else ''
                
                # Extraer descripción
                desc_elem = card.find('div', class_='card-body')
                workflow['description'] = desc_elem.text.strip() if desc_elem else ''
                
                # Extraer complejidad
                complexity_elem = card.find('span', class_=re.compile(r'tag complexity-.*'))
                workflow['complexity'] = complexity_elem.text.strip() if complexity_elem else ''
                
                # Extraer nodos
                nodes_elem = card.find('span', class_='tag nodes')
                workflow['nodes'] = nodes_elem.text.strip() if nodes_elem else ''
                
                # Solo agregar si tiene información mínima requerida y no es duplicado
                if workflow['filename'] and workflow['link']:
                    # Verificar si ya hemos visto este workflow
                    if workflow['filename'] not in seen_filenames:
                        workflows.append(workflow)
                        seen_filenames.add(workflow['filename'])
                        logger.debug(f"Workflow extraído: {workflow['filename']}")
                    else:
                        duplicate_count += 1
                        logger.info(f"Workflow duplicado omitido: {workflow['filename']}")
                else:
                    logger.warning("Tarjeta incompleta encontrada, omitiendo...")
                    
            except Exception as e:
                logger.error(f"Error al procesar tarjeta: {e}")
                continue
        
        if duplicate_count > 0:
            logger.info(f"Se encontraron y omitieron {duplicate_count} workflows duplicados")
                
        return workflows
    
    def extract_with_regex(self) -> List[Dict[str, str]]:
        """
        Extrae información usando expresiones regulares (método alternativo).
        Mantiene compatibilidad con el código original pero mejorado.
        Elimina duplicados basándose en el nombre del archivo.
        
        Returns:
            Lista de diccionarios con la información de cada workflow (sin duplicados)
        """
        workflows = []
        seen_filenames = set()  # Para rastrear workflows ya procesados
        duplicate_count = 0
        
        # Patrones mejorados y más específicos
        card_pattern = re.compile(
            r'<div class="workflow-card">(.*?)</div>\s*</div>', 
            re.DOTALL
        )
        
        # Patrones más específicos para evitar ambigüedades
        patterns = {
            'link': re.compile(r'<a href="([^"]+)"'),
            'filename': re.compile(r'<a[^>]*>\s*<span>([^<]+)</span>'),
            'description': re.compile(r'<div class="card-body">([^<]+)</div>'),
            'complexity': re.compile(r'<span class="tag complexity-[^"]*">([^<]+)</span>'),
            'nodes': re.compile(r'<span class="tag nodes">([^<]+)</span>')
        }
        
        # Buscar todas las tarjetas
        for match in card_pattern.finditer(self.html_content):
            card_html = match.group(1)
            workflow = {}
            
            # Extraer cada campo
            for field, pattern in patterns.items():
                field_match = pattern.search(card_html)
                workflow[field] = field_match.group(1).strip() if field_match else ''
            
            # Validar campos requeridos y verificar duplicados
            if workflow.get('filename') and workflow.get('link'):
                if workflow['filename'] not in seen_filenames:
                    workflows.append(workflow)
                    seen_filenames.add(workflow['filename'])
                    logger.debug(f"Workflow extraído (regex): {workflow['filename']}")
                else:
                    duplicate_count += 1
                    logger.info(f"Workflow duplicado omitido (regex): {workflow['filename']}")
            else:
                logger.warning("Tarjeta incompleta encontrada (regex), omitiendo...")
        
        if duplicate_count > 0:
            logger.info(f"Se encontraron y omitieron {duplicate_count} workflows duplicados")
                
        return workflows
    
    def to_markdown(self, workflows: List[Dict[str, str]]) -> str:
        """
        Convierte la lista de workflows a formato Markdown.
        
        Args:
            workflows: Lista de diccionarios con información de workflows
            
        Returns:
            String con el contenido en formato Markdown
        """
        if not workflows:
            return "# No se encontraron workflows\n"
        
        markdown_lines = ["# Workflows Disponibles\n"]
        markdown_lines.append(f"Total de workflows únicos: {len(workflows)}\n")
        markdown_lines.append("---\n")
        
        # Ordenar workflows por nombre para mejor organización
        sorted_workflows = sorted(workflows, key=lambda x: x.get('filename', '').lower())
        
        for workflow in sorted_workflows:
            markdown_lines.append(f"### [{workflow.get('filename', 'Sin nombre')}]({workflow.get('link', '#')})\n")
            
            if workflow.get('description'):
                markdown_lines.append(f"- **Descripción:** {workflow['description']}\n")
            
            if workflow.get('complexity'):
                markdown_lines.append(f"- **Complejidad:** {workflow['complexity']}\n")
            
            if workflow.get('nodes'):
                markdown_lines.append(f"- **Nodos:** {workflow['nodes']}\n")
            
            markdown_lines.append(f"- **URL:** {workflow.get('link', 'No disponible')}\n")
            markdown_lines.append("\n")
        
        return ''.join(markdown_lines)
    
    def process(self, use_beautifulsoup: bool = True) -> Optional[str]:
        """
        Procesa el archivo HTML y retorna el contenido en Markdown.
        
        Args:
            use_beautifulsoup: Si True, usa BeautifulSoup; si False, usa regex
            
        Returns:
            String con el contenido en Markdown o None si hay error
        """
        if not self.read_html_file():
            return None
        
        try:
            if use_beautifulsoup:
                logger.info("Usando BeautifulSoup para la extracción...")
                workflows = self.extract_with_beautifulsoup()
            else:
                logger.info("Usando expresiones regulares para la extracción...")
                workflows = self.extract_with_regex()
            
            logger.info(f"Se extrajeron {len(workflows)} workflows únicos")
            
            # Mostrar estadísticas adicionales si hay workflows
            if workflows:
                complexities = {}
                for w in workflows:
                    comp = w.get('complexity', 'Sin definir')
                    complexities[comp] = complexities.get(comp, 0) + 1
                
                logger.info("Distribución de complejidad:")
                for comp, count in sorted(complexities.items()):
                    logger.info(f"  - {comp}: {count} workflow(s)")
            
            return self.to_markdown(workflows)
            
        except Exception as e:
            logger.error(f"Error durante el procesamiento: {e}")
            return None


def main():
    """Función principal con interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Extrae información de workflows desde HTML a Markdown'
    )
    parser.add_argument(
        'html_file',
        nargs='?',
        default='/Users/jaimerestrepo/Proyectos/n8n-workflows-es/workflows/recursos.html',
        help='Ruta al archivo HTML a procesar'
    )
    parser.add_argument(
        '-o', '--output',
        help='Archivo de salida para el Markdown (opcional)'
    )
    parser.add_argument(
        '--use-regex',
        action='store_true',
        help='Usar expresiones regulares en lugar de BeautifulSoup'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Mostrar información detallada de depuración'
    )
    
    args = parser.parse_args()
    
    # Configurar nivel de logging
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Crear extractor y procesar
    extractor = WorkflowExtractor(args.html_file)
    markdown_output = extractor.process(use_beautifulsoup=not args.use_regex)
    
    if markdown_output:
        if args.output:
            # Guardar en archivo
            try:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(markdown_output)
                logger.info(f"Resultado guardado en: {args.output}")
            except Exception as e:
                logger.error(f"Error al guardar el archivo: {e}")
                sys.exit(1)
        else:
            # Imprimir en consola
            print(markdown_output)
    else:
        logger.error("No se pudo procesar el archivo")
        sys.exit(1)


if __name__ == "__main__":
    main()