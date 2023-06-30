import flet as ft 

last = ''

operation = 0

def main(page: ft.page):

    page.title = 'Calculadora'

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    numbers = {
        'zero': ft.Text(value='0'),
        'one': ft.Text(value='1'),
        'two': ft.Text(value='2'),
        'three': ft.Text(value='3'),
        'four': ft.Text(value='4'),
        'five': ft.Text(value='5'),
        'six': ft.Text(value='6'),
        'seven': ft.Text(value='7'),
        'eight': ft.Text(value='8'),
        'nine': ft.Text(value='9')
    }
    operators = {
        'comma': ft.Text(value=','),
        'plus': ft.Text(value='+'),
        'minus': ft.Text(value='-'),
        'multiply': ft.Text(value='x'),
        'divisor': ft.Text(value='/'),
        'equals': ft.Text(value='='),
        'percent': ft.Text(value='%'),
        'erase': ft.Text(value='C')
    }

    def number_zero(e):
        if txt_box.value != '0':
            txt_box.value += '0'
        else:
            txt_box.value = '0'
        page.update()

    def number_one(e):
        if txt_box.value == '0':
            txt_box.value = '1'
        else:
            txt_box.value += '1'
        page.update()
    
    def number_two(e):
        if txt_box.value == '0':
            txt_box.value = '2'
        else:
            txt_box.value += '2'
        page.update()
    
    def number_three(e):
        if txt_box.value == '0':
            txt_box.value = '3'
        else:
            txt_box.value += '3'
        page.update()
    
    def number_four(e):
        if txt_box.value == '0':
            txt_box.value = '4'
        else:
            txt_box.value += '4'
        page.update()
    
    def number_five(e):
        if txt_box.value == '0':
            txt_box.value = '5'
        else:
            txt_box.value += '5'
        page.update()
    
    def number_six(e):
        if txt_box.value == '0':
            txt_box.value = '6'
        else:
            txt_box.value += '6'
        page.update()
    
    def number_seven(e):
        if txt_box.value == '0':
            txt_box.value = '7'
        else:
            txt_box.value += '7'
        page.update()
    
    def number_eight(e):
        if txt_box.value == '0':
            txt_box.value = '8'
        else:
            txt_box.value += '8'
        page.update()

    def number_nine(e):
        if txt_box.value == '0':
            txt_box.value = '9'
        else:
            txt_box.value += '9'
        page.update()
    
    def plus_button(e):
        global operation, last
        if operation == 0:
            operation = int(txt_box.value)
            txt_box.value = '0'
        else:
            operation += int(txt_box.value)
            txt_box.value = '0'
        last = 'plus'
        page.update()

    def minus_button(e):
        global operation, last
        if operation == 0:
            operation = int(txt_box.value)
            txt_box.value = '0'
        else:
            operation -= int(txt_box.value)
            txt_box.value = '0'
        last = 'minus'
        page.update()
    
    def equals_button(e):
        global operation
        if last == 'plus':
            operation += (int(txt_box.value))
        elif last == 'minus':
            operation -= (int(txt_box.value))
        txt_box.value = str(operation)
        page.update()
        operation = 0
        txt_box.value = '0'
    
    def erase_button(e):
        global operation
        operation = 0
        txt_box.value = '0'
        page.update()
    
    txt_box = ft.TextField(text_align=ft.TextAlign.RIGHT, width=220, value='0', bgcolor='black')

    page.add(
        ft.Row(controls=
            [
                txt_box
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(controls=
            [
                ft.ElevatedButton(text=operators['erase'].value, width=50, on_click=erase_button),
                ft.ElevatedButton(text='', width=50),
                ft.ElevatedButton(text='', width=50),
                ft.ElevatedButton(text=operators['divisor'].value, width=50)
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(controls=
            [
                ft.ElevatedButton(text=numbers['seven'].value, width=50, on_click=number_seven),
                ft.ElevatedButton(text=numbers['eight'].value, width=50, on_click=number_eight),
                ft.ElevatedButton(text=numbers['nine'].value, width=50, on_click=number_nine),
                ft.ElevatedButton(text=operators['multiply'].value, width=50)
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(controls=
            [
                ft.ElevatedButton(text=numbers['four'].value, width=50, on_click=number_four),
                ft.ElevatedButton(text=numbers['five'].value, width=50, on_click=number_five),
                ft.ElevatedButton(text=numbers['six'].value, width=50, on_click=number_six),
                ft.ElevatedButton(text=operators['minus'].value, width=50, on_click=minus_button)
            ],
            alignment = ft.MainAxisAlignment.CENTER
            )
    )

    page.add(
        ft.Row(controls=
            [
                ft.ElevatedButton(text=numbers['one'].value, width=50, on_click=number_one),
                ft.ElevatedButton(text=numbers['two'].value, width=50, on_click=number_two),
                ft.ElevatedButton(text=numbers['three'].value, width=50, on_click=number_three),
                ft.ElevatedButton(text=operators['plus'].value, width=50, on_click=plus_button)
            ],
            alignment = ft.MainAxisAlignment.CENTER
            )
    )

    page.add(
        ft.Row(controls=
            [
                ft.ElevatedButton(text=numbers['zero'].value, width=100, on_click=number_zero),
                ft.ElevatedButton(text=operators['comma'].value, width=50),
                ft.ElevatedButton(text=operators['equals'].value, width=50, on_click=equals_button)
            ],
            alignment = ft.MainAxisAlignment.CENTER
            )
    )

ft.app(target=main)