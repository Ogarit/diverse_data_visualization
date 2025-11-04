# Diverse Data Visualization

## Descrição

Este repositório contém uma coleção de visualizações de dados diversas, utilizando Python e bibliotecas especializadas para explorar e apresentar dados de forma eficaz. O projeto demonstra exemplos de gráficos e visualizações interativas, com suporte a automação de GUI via PyAutoGUI e integração com Qt para ambientes Wayland.

## Funcionalidades

- Visualizações de dados com Matplotlib e Plotly.
- Manipulação de dados utilizando Pandas.
- Automação de interações GUI com PyAutoGUI.
- Suporte a ambientes gráficos Wayland via Qt6.

## Tecnologias Utilizadas

- Python (>=3.14.0, <3.15)
- Matplotlib (>=3.9.2, <4)
- Qt6-Wayland (>=6.7.3, <7)
- PyAutoGUI (>=0.9.54, <0.10)
- Plotly (>=5.24.1, <6)
- Pandas (>=2.2.3, <3)

## Instalação

Este projeto é gerenciado com [Pixi](https://pixi.sh/), uma ferramenta de gerenciamento de pacotes que utiliza Conda para dependências.

1. **Instale o Pixi:**  
   Siga as instruções no site oficial: [pixi.sh](https://pixi.sh/) ou no repositório GitHub [prefix-dev/pixi](https://github.com/prefix-dev/pixi). Para instalação rápida em sistemas Unix-like:  
   ```
   curl -fsSL https://pixi.sh/install.sh | bash
   ```  
   Para Windows, baixe o executável do GitHub.

2. **Clone o repositório:**  
   ```
   git clone https://github.com/Ogarit/diverse_data_visualization.git
   cd diverse_data_visualization
   ```

3. **Instale as dependências:**  
   ```
   pixi install
   ```  
   Isso criará um ambiente virtual com todas as dependências especificadas no `pixi.toml`, usando os canais `https://conda.modular.com/max-nightly` e `conda-forge`.

## Uso

Ative o ambiente Pixi:  
```
pixi shell
```

Em seguida, execute com `pixi run python {script_name}.py`.

## Contribuição

Contribuições são bem-vindas! Para contribuir:  
1. Faça um fork do repositório.  
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).  
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).  
4. Push para a branch (`git push origin feature/nova-feature`).  
5. Abra um Pull Request.  

Por favor, siga as boas práticas de código e teste suas mudanças.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Se o arquivo LICENSE não estiver presente, assume-se a licença MIT padrão.
