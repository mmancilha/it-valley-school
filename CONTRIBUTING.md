# Guia de Contribuição

Bem-vindo ao projeto abrangente de IA/ML! Este guia fornece diretrizes completas para contribuir com esta iniciativa de inteligência artificial que engloba análise de emoções, detecção de gênero, processamento de imagens e múltiplas técnicas de machine learning.

## 🎯 Visão Geral do Projeto

Este repositório contém implementações avançadas de inteligência artificial e machine learning, incluindo:
- **Análise de Emoções**: Classificação de felicidade/tristeza com múltiplos algoritmos
- **Detecção de Gênero**: Visão computacional com OpenCV para classificação de gênero
- **Comparação de Algoritmos**: Regressão Logística, SVM, Random Forest e Deep Learning
- **Processamento de Imagens**: Técnicas avançadas com OpenCV
- **Metodologias Diversas**: Abordagens variadas de IA/ML

Acolhemos contribuições que aprimorem o desempenho dos modelos, qualidade do código e documentação.

## 🚀 Primeiros Passos

### Pré-requisitos
- Python 3.8+
- Git
- Ambiente virtual (obrigatório)
- OpenCV, scikit-learn, pandas, numpy

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
Use mensagens de commit descritivas seguindo conventional commits:
```
type(scope): descrição breve

Descrição detalhada se necessário
```

Exemplos:
- `feat(model): implementar classificador Random Forest`
- `docs(readme): atualizar documentação de instalação`
- `fix(preprocessing): corrigir lógica de tokenização de texto`
- `perf(training): otimizar pipeline de treinamento do modelo`

### Padrões de Código
- Seguir PEP 8 para código Python
- Usar nomes descritivos para variáveis e funções
- Adicionar comentários abrangentes para algoritmos complexos
- Incluir docstrings para todas as funções e classes
- Manter formatação consistente do código

### Requisitos de Documentação
- Manter README.md atualizado com mudanças do projeto
- Documentar novos modelos com métricas de desempenho
- Incluir exemplos de uso para novas funcionalidades
- Manter precisão técnica em toda documentação

## 🔬 Adicionando Novos Modelos

### Estrutura de Arquivos
```python
"""
Descrição e objetivo do modelo
Autor: [Seu Nome]
Data: [Data]
"""

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
# Importações adicionais conforme necessário

def preprocess_data(data_path):
    """Pipeline de pré-processamento de dados"""
    pass

def train_model(X_train, y_train, **kwargs):
    """Treinamento do modelo com hiperparâmetros"""
    pass

def evaluate_model(model, X_test, y_test):
    """Avaliação abrangente do modelo"""
    pass

if __name__ == "__main__":
    # Pipeline principal de execução
    pass
```

### Métricas Obrigatórias
- Pontuação de acurácia
- Tempo de treinamento
- Tamanho e características do dataset
- Parâmetros e hiperparâmetros do modelo
- Uso de memória (para modelos grandes)

## 📊 Padrões de Avaliação

### Métricas de Desempenho
Todos os modelos devem reportar:
- Acurácia do conjunto de teste
- Matriz de confusão
- Tempo de treinamento
- Tempo de inferência
- Uso de memória (quando aplicável)
- Pontuações de validação cruzada

### Formato de Saída
```
=== RESULTADOS DE AVALIAÇÃO DO MODELO ===
Modelo: [Nome do Modelo]
Dataset: [Tamanho e descrição]
Acurácia: [X.XX%]
Tempo de Treinamento: [X.X segundos]
Tempo de Inferência: [X.X ms/amostra]
Parâmetros: [Configurações principais]
Validação Cruzada: [Média ± Desvio]
```

## 🔧 Fluxo de Desenvolvimento

### Estratégia de Branches
- `main`: Código pronto para produção
- `develop`: Branch de integração para funcionalidades
- `feature/*`: Desenvolvimento de funcionalidades individuais
- `hotfix/*`: Correções críticas de bugs

### Processo de Pull Request
1. Fazer fork do repositório
2. Criar uma branch de funcionalidade
3. Implementar mudanças com testes
4. Atualizar documentação
5. Submeter pull request com descrição detalhada
6. Abordar feedback da revisão

### Pipeline de Desenvolvimento de Modelos
1. **Baseline**: Modelos simples (Regressão Logística)
2. **Aprimoramento**: Algoritmos avançados (SVM, Random Forest)
3. **Deep Learning**: Redes neurais e modelos profundos
4. **Otimização**: Ajuste de hiperparâmetros e engenharia de features

## 🌍 Padrões de Qualidade

### Qualidade do Código
- Código limpo e bem documentado
- Testes unitários para funções críticas
- Versionamento adequado de modelos
- Resultados reproduzíveis com gerenciamento de seed
- Benchmarking de desempenho

### Padrões de Documentação
- Atualizações abrangentes do README
- Documentação inline do código
- Documentos de especificação técnica
- Exemplos claros de uso
- Documentação de API para componentes reutilizáveis

## 🧪 Diretrizes de Testes

### Requisitos de Testes
- Testes unitários para funções de pré-processamento de dados
- Testes de validação de modelos
- Testes de integração para pipelines completos
- Testes de regressão de desempenho

### Executando Testes
```bash
# Executar todos os testes
python -m pytest tests/

# Executar categoria específica de testes
python -m pytest tests/test_models.py

# Executar com cobertura
python -m pytest --cov=src tests/
```

## 📞 Contato e Suporte

Para dúvidas, sugestões ou colaboração:
- **Email**: mancilhamaycon@gmail.com
- **LinkedIn**: [linkedin.com/in/mayconmancilha](https://www.linkedin.com/in/mayconmancilha/)
- **GitHub**: [@mmancilha](https://github.com/mmancilha)

## 📄 Licença

Este projeto é open source e está disponível sob a Licença MIT.

---

*Obrigado por contribuir com este projeto abrangente de IA/ML! Suas contribuições ajudam a avançar o estado da arte em análise de emoções, detecção de gênero e técnicas diversas de inteligência artificial.*