
### **
# Curso de NumPy para Análise de Dados

Bem-vindo ao repositório do Curso de NumPy! Este material foi criado para oferecer uma introdução prática e direta à biblioteca NumPy, uma das ferramentas mais fundamentais para computação científica e análise de dados em Python.

## 🎯 Objetivo do Curso

O objetivo deste curso é capacitar você a utilizar os principais recursos do NumPy para manipulação e análise de arrays multidimensionais de forma eficiente. Ao final do curso, você terá uma base sólida para aplicar NumPy em projetos de machine learning, análise de dados, processamento de sinais e muito mais.

## 📚 Conteúdo do Curso

O curso é dividido em uma série de Jupyter Notebooks, cada um focado em um aspecto específico da biblioteca. A estrutura é a seguinte:

1.  **`01-numpy-introducao.ipynb`**: Introdução aos conceitos básicos do NumPy e a importância dos arrays.
2.  **`02-numpy-arrays.ipynb`**: Criação, indexação e manipulação de arrays NumPy.
3.  **`03-numpy-funcoes.ipynb`**: Exploração das funções universais (ufuncs) e outras funções matemáticas essenciais.
4.  **`04-numpy-estatistica-basica.ipynb`**: Utilização do NumPy para cálculos estatísticos fundamentais como média, mediana, desvio padrão, etc.
5.  **`05-numpy-algebra-linear.ipynb`**: Aplicações de NumPy em operações de Álgebra Linear, como produto escalar e inversão de matrizes.
6.  **`06-numpy-copia-view.ipynb`**: Entendendo a diferença crucial entre cópias (`copy`) e visualizações (`view`) de arrays.

## 🚀 Como Começar

Para seguir este curso, você precisará ter o [Poetry](https://www.google.com/search?q=https://python-poetry.org/docs/%23installation) instalado em sua máquina. O Poetry cuidará da instalação do Python (se necessário), das dependências e do gerenciamento do ambiente virtual.

**1. Clone este repositório:**

```
git clone https://github.com/marcelosanto/numpy-curso.git
cd numpy-curso
```

**2. Instale as dependências com Poetry:** Este comando irá ler o arquivo `pyproject.toml` (se não existir, você pode criá-lo com `poetry init`), resolver as dependências e instalá-las em um ambiente virtual dedicado.

_Primeiro, adicione as bibliotecas necessárias ao seu projeto:_


```
poetry add numpy pandas jupyterlab
```

_Depois, instale tudo:_


```
poetry install
```

**3. Execute o Jupyter Lab:** Para garantir que você está usando as bibliotecas do ambiente virtual criado pelo Poetry, execute o Jupyter Lab através do próprio Poetry.


```
poetry run jupyter lab

```

Alternativamente, você pode ativar o shell do ambiente virtual primeiro e depois rodar o comando:
 
```
poetry shell
jupyter lab
```

Pronto! Seu navegador abrirá uma nova aba com o ambiente Jupyter. Agora é só navegar pelos notebooks na ordem proposta e começar a aprender!