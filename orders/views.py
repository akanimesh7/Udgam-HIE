from django.shortcuts import render
from. models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.core import mail
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.template import Context
@login_required
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order=form.save()

			for item in cart:
				OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
			cart.clear()
			subject="Thank you for shopping with eKraft"
			from_email=settings.EMAIL_HOST_USER
			to_email=[order.email]
			signup_message="""Thank You For your Purchase with us . Your order will be delivered in next 10 days."""
			send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False, )
			return render(request, 'orders/order/created.html', {'order':order})
		return HttpResponse("You Have filled the form incorrectly. PLease go back and fill the form correctly. Please give genuine email address and integer in postal code")

	else:
		form=OrderCreateForm()
		return render(request, 'orders/order/create.html', {'form':form})
	#return HttpResponse("hi")
