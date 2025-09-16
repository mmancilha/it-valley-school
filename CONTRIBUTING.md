# Guia de Contribuição

Bem-vindo ao projeto de Análise de Emoções! Este documento fornece diretrizes para contribuir com este projeto acadêmico.

## 🎯 Contexto Acadêmico

Este projeto faz parte do programa de pós-graduação em Inteligência Artificial & Machine Learning da IT Valley School. O foco está em demonstrar aprendizado progressivo e implementação de melhores práticas da indústria.

## 🚀 Começando

### Pré-requisitos
- Python 3.8+
- Git
- Ambiente virtual (recomendado)

### Configuração do Ambiente

```bash
# Clonar o repositório
git clone https://github.com/mmancilha/it-valley-school.git
cd it-valley-school

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## 📝 Diretrizes de Contribuição

### Estrutura de Commits
Use mensagens de commit descritivas seguindo o padrão:
```
tipo(escopo): descrição breve

Descrição mais detalhada se necessário
```

Exemplos:
- `feat(model): adicionar modelo Random Forest`
- `docs(readme): atualizar documentação de instalação`
- `fix(preprocessing): corrigir tokenização de texto`

### Padrões de Código
- Siga PEP 8 para código Python
- Use nomes de variáveis descritivos
- Adicione comentários para lógica complexa
- Inclua docstrings para funções e classes

### Documentação
- Mantenha o README.md atualizado
- Documente novos modelos na pasta `docs/`
- Inclua métricas de performance para novos modelos
- Use português para documentação principal

## 🔬 Adicionando Novos Modelos

### Estrutura de Arquivo
```python
"""
Descrição do modelo e objetivo
"""

import numpy as np
import pandas as pd
# outros imports necessários

def preprocess_data():
    """Pré-processamento dos dados"""
    pass

def train_model():
    """Treinamento do modelo"""
    pass

def evaluate_model():
    """Avaliação do modelo"""
    pass

if __name__ == "__main__":
    # Execução principal
    pass
```

### Métricas Obrigatórias
- Acurácia
- Tempo de treinamento
- Tamanho do dataset
- Parâmetros do modelo

## 📊 Padrões de Avaliação

### Métricas de Performance
Todos os modelos devem reportar:
- Acurácia no conjunto de teste
- Matriz de confusão
- Tempo de treinamento
- Uso de memória (se relevante)

### Formato de Saída
```
=== RESULTADOS DO MODELO ===
Modelo: [Nome do Modelo]
Dataset: [Tamanho e descrição]
Acurácia: [X.XX%]
Tempo de Treinamento: [X.X segundos]
Parâmetros: [Configurações principais]
```

## 🎓 Objetivos Educacionais

### Foco de Aprendizado
- Implementação de algoritmos de ML
- Comparação de performance entre modelos
- Melhores práticas de código
- Documentação técnica
- Preparação para mercado internacional

### Progressão Esperada
1. **Baseline**: Modelos simples (Regressão Logística)
2. **Melhoria**: Algoritmos mais sofisticados (SVM, Random Forest)
3. **Avançado**: Deep Learning e redes neurais
4. **Otimização**: Tuning de hiperparâmetros e feature engineering

## 🌍 Padrões Internacionais

### Qualidade de Código
- Código limpo e bem documentado
- Testes unitários quando aplicável
- Versionamento adequado de modelos
- Reprodutibilidade dos resultados

### Documentação
- README abrangente
- Comentários em inglês no código
- Documentação técnica detalhada
- Exemplos de uso claros

## 📞 Contato

Para dúvidas ou sugestões:
- **Email**: mancilhamaycon@gmail.com
- **LinkedIn**: [linkedin.com/in/mayconmancilha](https://www.linkedin.com/in/mayconmancilha/)
- **GitHub**: [@mmancilha](https://github.com/mmancilha)

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do programa de pós-graduação da IT Valley School.

---

*Obrigado por contribuir com este projeto acadêmico! Seu envolvimento ajuda a demonstrar colaboração e melhores práticas da indústria.*