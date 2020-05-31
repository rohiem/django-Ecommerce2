from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')

)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(required=False,
                                                                              widget=CountrySelectWidget(attrs={"class": 'custom-select d-black w-100'}))
    shipping_zip = forms.CharField(required=False)
#    same_shipping_address = forms.BooleanField(widget=forms.CheckboxInput())
#    save_info = forms.BooleanField(widget=forms.CheckboxInput())
#    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False, widget=CountrySelectWidget(attrs={"class": 'custom-select d-black w-100'}))
#    billing_country = CountryField(blank_label='(select country)').formfield(required=False,widget=CountrySelectWidget(attrs={"class": 'custom-select d-black w-100'}))
    billing_zip = forms.CharField(required=False)
#    same_shipping_address = forms.BooleanField(widget=forms.CheckboxInput())
    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "promo code",
        "aria-label": "recipient's user name",
        "aria-describedby": "basic-addon2"
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 85}), max_length=160)
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
