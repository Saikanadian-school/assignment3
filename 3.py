import ui

def calculate_button_touch_up_inside(sender):
    
    HST = 0.13
    size = int(view['size_textfield'].text)
    topping = int(view['topping_textfield'].text)
    
    sub_total = size + topping
    cost = sub_total + (sub_total * HST)
    view['total'].text = 'The cost is: ' + '${:,.2f}'.format(cost)

view = ui.load_view()
view.present('full_screen')
