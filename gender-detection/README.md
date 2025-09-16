# Projeto de Detecção de Gênero

Um projeto de machine learning para classificação de gênero usando técnicas de visão computacional e algoritmo Support Vector Machine (SVM).

## Visão Geral do Projeto

Este projeto implementa um sistema de classificação binária para distinguir entre rostos masculinos e femininos usando processamento de imagens e técnicas de machine learning.

## Detalhes Técnicos

### Dataset
- **Dados de Treino**: 10 imagens de homens + 10 imagens de mulheres
- **Total de Amostras**: 20 imagens
- **Divisão dos Dados**: 80% treino (16 imagens) / 20% teste (4 imagens)

### Pipeline de Processamento de Imagens
1. **Conversão para Tons de Cinza**: Todas as imagens são convertidas para tons de cinza para reduzir complexidade
2. **Padronização**: Imagens são redimensionadas para 64x64 pixels para consistência
3. **Vetorização**: Cada imagem 64x64 é achatada em um vetor 1D de 4.096 características (64 × 64 = 4.096)
4. **Normalização**: Valores dos pixels são normalizados para o intervalo [0,1] dividindo por 255

### Modelo de Machine Learning
- **Algoritmo**: Support Vector Machine (SVM) com kernel RBF
- **Características**: Vetores de 4.096 dimensões (imagens 64x64 em tons de cinza achatadas)
- **Rótulos**: Classificação binária (0 = Masculino, 1 = Feminino)
- **Treinamento**: 80% dos dados (16 amostras)
- **Teste**: 20% dos dados (4 amostras)

### O que é o Vetor de 4.096?
O valor 4.096 representa o número total de pixels em uma imagem 64x64:
- Cada imagem tem 64 pixels de largura × 64 pixels de altura = 4.096 pixels totais
- Quando achatada, isso cria um vetor com 4.096 características numéricas
- Cada característica representa a intensidade de tons de cinza de um pixel (intervalo 0-1)

## Estrutura do Projeto

```
gender-detection/
├── imagens/
│   ├── homem/          # Fotos de homens (10 imagens)
│   └── mulher/         # Fotos de mulheres (10 imagens)
├── modelos/            # Modelos treinados serão salvos aqui
├── 1 - opencvCore.py   # Básicos do OpenCV
├── 2 - opencv2draw.py  # Funções de desenho
├── 3 - tratarImagem.py # Utilitários de processamento de imagem
├── 4 - treinar-salvar.py # Script principal de treinamento
├── README.md
├── README-PT.md        # Documentação em português
└── requirements.txt
```

## Como Usar

1. **Preparar Dataset**: Coloque suas imagens nas pastas correspondentes:
   - Fotos de homens → `imagens/homem/`
   - Fotos de mulheres → `imagens/mulher/`

2. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar Treinamento**:
   ```bash
   python "4 - treinar-salvar.py"
   ```

4. **Saída Esperada**:
   ```
   ✅ Carregadas 10 fotos de homens
   ✅ Carregadas 10 fotos de mulheres
   Dados de treino: 16 imagens
   Dados de teste: 4 imagens
   ```

## Dependências

- **OpenCV (cv2)**: Processamento de imagens e visão computacional
- **NumPy**: Computações numéricas e operações com arrays
- **Scikit-learn**: Algoritmos de machine learning (SVM, train_test_split)
- **OS**: Operações do sistema de arquivos

## Resultados

Com o dataset atual:
- **Total de Imagens**: 20 (10 homens + 10 mulheres)
- **Conjunto de Treino**: 16 imagens (80%)
- **Conjunto de Teste**: 4 imagens (20%)
- **Dimensão das Características**: 4.096 por imagem
- **Modelo**: SVM com kernel RBF