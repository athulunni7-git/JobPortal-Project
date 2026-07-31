from django.shortcuts import render , redirect
from django.views import View
from django.conf import settings
import razorpay
from payment.models import Payment
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

# Create your views here.

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))



class PremiumPlanView(View):
    
    def get(self,request):
        
        if not request.user.is_authenticated:
            if not request.user.is_authenticated:
                return redirect('account:userlogin')

        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access Premium.")
            return redirect('home')
        
        
        return render(request,'premiumplans.html')
            


class CreateOrderView(View):
    
    def get(self,request,plan):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')

        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can buy premium.")
            return redirect('home')
        
        if plan == "monthly":
            amount = 499
            
        elif plan == 'yearly':
            amount = 4999
        else:
            messages.error(request, "Invalid Plan")
            return redirect('payment:premium')
        
        razorpay_order = client.order.create({ 'amount':amount*100,'currency':'INR'})
        
        payment = Payment.objects.create(user=request.user,
                                         amount=amount,
                                         plan=plan,
                                         razorpay_order_id=razorpay_order['id'],
                                         status='pending')
        
        context = {"payment": payment,
                    "razorpay_order": razorpay_order,
                    "razorpay_key": settings.RAZORPAY_KEY_ID,
                    "amount": amount}
        
        return render(request,'payment.html',context)
           
        
class PaymentSuccessView(View):
    
    def post(self,request):
        
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        
            
        data = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature,
        }
        
        try:
            client.utility.verify_payment_signature(data)
            payment = Payment.objects.get(razorpay_order_id = razorpay_order_id)
            
            payment.razorpay_payment_id = razorpay_payment_id
            payment.razorpay_signature = razorpay_signature
            payment.status = "success"
            payment.save()
            
            
            recruiter = request.user.recruiterprofile

            recruiter.is_premium = True
            recruiter.premium_start = timezone.now()

            if payment.plan == "monthly":
                recruiter.premium_plan = "monthly"
                recruiter.premium_end = timezone.now() + timedelta(days=30)

            else:
                recruiter.premium_plan = "yearly"
                recruiter.premium_end = timezone.now() + timedelta(days=365)

            recruiter.save()

            messages.success(request, "Premium Membership Activated Successfully.")

            return redirect("account:recruiter_dashboard")
        
        except Exception as e:
            print(e)
            messages.error(request, "Payment Verification Failed.")
            return redirect("payment:premium")

            return redirect("payment:premium")

        
        