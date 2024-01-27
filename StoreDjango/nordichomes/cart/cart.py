from django.conf import settings
#---------------------------------
from product.models import Product

class Cart(object):
    #---constructor-----------
    def __init__(self, request):
        # ------create session for the cart------
        self.session = request.session
        #----create the cart object--------------
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # create an empty dictionary
            cart = self.session[settings.CART_SESSION_ID]={}
        #-----attribute of cart
        self.cart = cart
    #----iterator------acsesss to data base---------
    def __iter__(self):
        # iterate over the keys in dict (cart)
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
     # return the total quantity of products in the cart   
    def __len__(self):
        # iterate over the values of products in the cart
        return sum(item['quantity'] for item in self.cart.values())
    
    # notify the browser that something happend with the session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    # add products to the cart
    def add(self, product_id, quantity = 1, update_quantity = False):
        product_id = str(product_id) # stringify
        
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':1, 'id':product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] +=int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        self.save()

    #remove method
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

