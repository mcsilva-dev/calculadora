import flet as ft 

last = ''

operation = 0

def main(page: ft.Page):

    page.title = 'Calculadora'

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_max_height = 450
    page.window_max_width = 450

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
        'multiply': ft.Text(value='*'),
        'divisor': ft.Text(value='/'),
        'equals': ft.Text(value='='),
        'percent': ft.Text(value='%'),
        'erase': ft.Text(value='AC')
    }

    def number_zero(e):
        global operation
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
        if last == 'minus':
            operation -= float(txt_box.value)
            pass
        if operation == 0 and last == 'plus' or last == '':
            operation = float(txt_box.value)
        elif operation != 0 and last == 'plus':
            operation += float(txt_box.value)
        last = 'plus'
        page.update()
        txt_box.value = '0'

    def minus_button(e):
        global operation, last
        if last == 'plus':
            operation += float(txt_box.value)
            pass
        if operation == 0 and last == 'minus' or last == '':
            operation = float(txt_box.value)
        elif operation != 0 and last == 'minus':
            operation -= float(txt_box.value)
        last = 'minus'
        page.update()
        txt_box.value = '0'
    
    def equals_button(e):
        global operation, last
        if last == 'plus':
            operation += float(txt_box.value)
        elif last == 'minus':
            operation -= float(txt_box.value)
        txt_box.value = str(operation)
        page.update()
        txt_box.value = '0'
    
    def comma_button(e):
        txt_box.value += '.'
        page.update()
    
    def erase_button(e):
        global operation, last
        operation = 0
        txt_box.value = '0'
        last = ''
        page.update()
    
    txt_box = ft.TextField(
                        text_align=ft.TextAlign.RIGHT, 
                        width=350, 
                        value='0', 
                        bgcolor='black'
                        )
    
    page.add(
        ft.Row(controls=
            [
                txt_box
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(controls=
            [
                ft.ElevatedButton(
                                text=operators['erase'].value,
                                width=80, on_click=erase_button, 
                                bgcolor=ft.colors.BLUE_GREY_100, 
                                color='black'
                                ),
                ft.ElevatedButton(
                                text='', width=80, 
                                bgcolor=ft.colors.BLUE_GREY_100, 
                                color='black'
                                ),
                ft.ElevatedButton(
                                text='', 
                                width=80, 
                                bgcolor=ft.colors.BLUE_GREY_100, 
                                color='black'
                                ),
                ft.ElevatedButton(
                                text=operators['divisor'].value, 
                                width=80, 
                                bgcolor='orange', 
                                color='white'
                                )
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(controls=
            [
                ft.ElevatedButton(
                                text=numbers['seven'].value,
                                width=80,
                                on_click=number_seven,
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=numbers['eight'].value, 
                                width=80, 
                                on_click=number_eight, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=numbers['nine'].value, 
                                width=80, 
                                on_click=number_nine, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=operators['multiply'].value, 
                                width=80, 
                                bgcolor='orange', 
                                color='white'
                                )
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(controls=
            [
                ft.ElevatedButton(
                                text=numbers['four'].value, 
                                width=80, 
                                on_click=number_four, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=numbers['five'].value, 
                                width=80, 
                                on_click=number_five, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=numbers['six'].value, 
                                width=80, on_click=number_six, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=operators['minus'].value, 
                                width=80, 
                                on_click=minus_button, 
                                bgcolor='orange', 
                                color='white')
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
        ft.Row(controls=
            [
                ft.ElevatedButton(
                                text=numbers['one'].value, 
                                width=80, 
                                on_click=number_one, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=numbers['two'].value, 
                                width=80, 
                                on_click=number_two, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=numbers['three'].value, 
                                width=80, on_click=number_three, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'),
                ft.ElevatedButton(
                                text=operators['plus'].value, 
                                width=80, 
                                on_click=plus_button, 
                                bgcolor='orange', 
                                color='white'
                                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
        ft.Row(controls=
            [
                ft.ElevatedButton(
                                text=numbers['zero'].value, 
                                width=170, on_click=number_zero, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white'
                                ),
                ft.ElevatedButton(
                                text=operators['comma'].value, 
                                width=80, 
                                bgcolor=ft.colors.WHITE24, 
                                color='white',
                                on_click=comma_button,
                                ),
                ft.ElevatedButton(
                                text=operators['equals'].value, 
                                width=80, on_click=equals_button, 
                                bgcolor='orange', 
                                color='white'
                                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )

    

ft.app(target=main)