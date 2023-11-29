#EXAMEN PROGRAMACIÓN WEB
#DILAN GATICA MOYA

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
    if request.method == 'POST':
        nombre = (request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        total_sn_dscto = (tarros*9000)
        saludo_cliente = f'Nombre del cliente:{nombre}'
        if edad >= 18 and edad <= 30:
            dscto = ((tarros*9000)/100)*15
            total_cn_dscto = (total_sn_dscto - dscto)
            return render_template('ejercicio_1.html', nombre=nombre, total1=f'El total sin dscto es: ${total_sn_dscto}',
                                   total2=f'Su dscto es de: ${dscto}', total3=f'El total a pagar es: ${total_cn_dscto}',
                                   edad=edad, tarros=tarros, saludo_cliente=saludo_cliente)
        elif edad > 30:
            dscto = ((tarros*9000)/100)*25
            total_cn_dscto = (total_sn_dscto - dscto)
            return render_template('ejercicio_1.html', nombre=nombre, total1=f'El total sin dscto es: ${total_sn_dscto}',
                                   total2=f'Su dscto es de: ${dscto}', total3=f'El total a pagar es: ${total_cn_dscto}',
                                   edad=edad, tarros=tarros, saludo_cliente=saludo_cliente)
        elif edad < 18:
            dscto = 0
            total_cn_dscto = (total_sn_dscto - dscto)
            return render_template('ejercicio_1.html', nombre=nombre, total1=f'El total sin dscto es: ${total_sn_dscto}',
                                   total2=f'Su dscto es de: ${dscto}', total3=f'El total a pagar es: ${total_cn_dscto}',
                                   edad=edad, tarros=tarros, saludo_cliente=saludo_cliente)
    return render_template('ejercicio_1.html')

@app.route('/ejercicio_2', methods=['GET','POST'])
def ejercicio_2():
    if request.method == 'POST':
        usuario = (request.form['usuario'])
        pass1 = (request.form['pass1'])
        if usuario == 'juan' and pass1 == 'admin':
            return render_template('ejercicio_2.html', usuario=usuario, resultado=f'Bienvenido Administrador Juan')
        elif usuario == 'pepe' and pass1 == 'user':
            return render_template('ejercicio_2.html', usuario=usuario, resultado=f'Bienvenido Usuario Pepe')
        else:
            return render_template('ejercicio_2.html', resultado='Usuario o Contraseña Incorrecta')
    return render_template('ejercicio_2.html')


if __name__ == '__main__':
    app.run(debug=True)

