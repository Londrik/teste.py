import flet as ft

def main(page: ft.Page):
    # Configurações da janela principal
    page.title = "Calculadora Flet"
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False
    page.bgcolor = ft.Colors.BLACK
    
    # Texto que serve como o visor da calculadora
    visor = ft.Text(value="0", color=ft.Colors.WHITE, size=40)

    # Função que lida com o clique de qualquer botão
    def botao_clicado(e):
        valor_botao = e.control.content.value

        # Limpar a tela
        if valor_botao == "C":
            visor.value = "0"
        
        # Apagar o último caractere
        elif valor_botao == "⌫":
            if len(visor.value) > 1:
                visor.value = visor.value[:-1]
            else:
                visor.value = "0"
                
        # Calcular o resultado
        elif valor_botao == "=":
            try:
                # Substitui os símbolos visuais e a vírgula pelos operadores do Python
                expressao = visor.value.replace("x", "*").replace("÷", "/").replace(",", ".")
                
                # Calcula o valor bruto da string
                resultado_bruto = eval(expressao)
                
                # Arredonda para 10 casas decimais para corrigir o erro de ponto flutuante (ex: 0,1 + 0,2)
                resultado = round(resultado_bruto, 10)
                
                # Se o resultado terminar em .0 (inteiro), remove os decimais desnecessários
                if resultado == int(resultado):
                    resultado = int(resultado)
                
                # Exibe o resultado voltando o ponto para vírgula padrão brasileira
                visor.value = str(resultado).replace(".", ",")
            except Exception:
                visor.value = "Erro"
                
        # Digitar números e operadores
        else:
            if visor.value == "0" or visor.value == "Erro":
                # Se for um operador ou vírgula, mantém o 0 na frente (ex: 0,1)
                if valor_botao in ["+", "-", "x", "÷", ","]:
                    visor.value = "0" + valor_botao
                else:
                    visor.value = valor_botao
            else:
                visor.value += valor_botao

        page.update()

    # Função auxiliar atualizada para o padrão ft.Button
    def criar_botao(texto, cor_fundo=ft.Colors.SURFACE_CONTAINER_HIGHEST, cor_texto=ft.Colors.WHITE):
        return ft.Button(
            content=ft.Text(texto, color=cor_texto, size=18, weight=ft.FontWeight.BOLD),
            bgcolor=cor_fundo,
            on_click=botao_clicado,
            expand=1, 
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=20
            )
        )

    # Layout da interface
    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    # Área do Visor
                    ft.Row(
                        controls=[visor],
                        alignment=ft.MainAxisAlignment.END
                    ),
                    ft.Divider(color=ft.Colors.GREY_800),
                    
                    # Linhas de botões
                    ft.Row(controls=[
                        criar_botao("C", ft.Colors.RED_ACCENT, ft.Colors.WHITE),
                        criar_botao("⌫", ft.Colors.BLUE_GREY),
                        criar_botao("(", ft.Colors.BLUE_GREY),
                        criar_botao(")", ft.Colors.BLUE_GREY),
                    ]),
                    ft.Row(controls=[
                        criar_botao("7"), criar_botao("8"), criar_botao("9"),
                        criar_botao("÷", ft.Colors.ORANGE, ft.Colors.WHITE)
                    ]),
                    ft.Row(controls=[
                        criar_botao("4"), criar_botao("5"), criar_botao("6"),
                        criar_botao("x", ft.Colors.ORANGE, ft.Colors.WHITE)
                    ]),
                    ft.Row(controls=[
                        criar_botao("1"), criar_botao("2"), criar_botao("3"),
                        criar_botao("-", ft.Colors.ORANGE, ft.Colors.WHITE)
                    ]),
                    # Linha com o zero, a vírgula, o igual e a soma (+)
                    ft.Row(controls=[
                        criar_botao("0"), 
                        criar_botao(","),
                        criar_botao("=", ft.Colors.ORANGE, ft.Colors.WHITE),
                        criar_botao("+", ft.Colors.ORANGE, ft.Colors.WHITE)
                    ]),
                ],
                spacing=10
            )
        )
    )

if __name__ == "__main__":
    ft.run(main)