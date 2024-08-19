from CAFFOOD.models.food import Food 
from CAFFOOD.models.order import Order
from CAFFOOD.models.order_item import OrderItem
from CAFFOOD.models.customer import Customer
from django.http import JsonResponse
from CAFFOOD.models.menu import Menu
from CAFFOOD.models.notification import Notification
import json



# Ananymous user add to cart 
def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0}
    total_cart = order['get_cart_items']

    for i in cart:  
        try:   
            total_cart += cart[i]['quantity']

            product = Food.objects.get(id=i)
            total   = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product' : {
                    'id': product.id,
                    'name':product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)
        except:
            pass 
    return {'items':items, 'order':order,'total_cart':total_cart}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        notification = Notification.objects.filter(user=customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total_cart = order.get_cart_items
    else:
        cookie_data = cookie_cart(request)
        items       = cookie_data['items']
        order       = cookie_data['order']
        total_cart  = cookie_data['total_cart']
        notification= ''
        notification_count=''
    return {'items':items, 'order':order,'total_cart':total_cart, 'notification':notification}

def notification(head, message, user):
    Notification.objects.create(user=user, head=head, message=message)
    return True