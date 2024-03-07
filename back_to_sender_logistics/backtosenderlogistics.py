def get_amount_per_parcel(number_of_deliveries):
    if number_of_deliveries < 50:
        return 160
    elif 50 <= number_of_deliveries < 60:
        return 200
    elif 60 <= number_of_deliveries < 70:
        return 250
    else:
        return 500


def validate_number_of_deliveries(number_of_deliveries):
    if number_of_deliveries < 0 or number_of_deliveries > 100:
        raise ValueError("Invalid input")


def payment_calculator(number_of_deliveries):
    try:
        base_pay = 5000
        validate_number_of_deliveries(number_of_deliveries)
        wage = (get_amount_per_parcel(number_of_deliveries) * number_of_deliveries) + base_pay
        return wage
    except ValueError:
        pass
