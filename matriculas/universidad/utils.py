import random
from datetime import date, timedelta

# archivo de utilidades

"""
    Estas funciones son para generar los datos de pago
"""
def generate_paycode():
    codigo = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return codigo

def generate_amount():
    return round(random.uniform(100, 1000), 2)

def generate_expiration_date():
    return date.today() + timedelta(weeks=1)


"""
    Estas funciones son para generar datos del estudiante que ya pago
"""

def generate_student_code():
    return generate_paycode()

def generate_email_student():
    return generate_student_code() + '@utp.pe'

def generate_student_password():
    return generate_paycode()
