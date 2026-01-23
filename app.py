from flask import Flask



# ===== PARTE 1: HTML/CSS/JAVASCRIPT (Interfaz) =====
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Flask</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            padding: 20px;
        }
        
        .container {
            width: 100%;
            max-width: 900px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .header {
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .header h1 {
            color: #2575fc;
            margin-bottom: 10px;
            font-size: 2.5rem;
        }
        
        .header p {
            color: #666;
            font-size: 1.1rem;
        }
        
        .calculator-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        
        .calculator {
            flex: 1;
            min-width: 300px;
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .calculator h2 {
            color: #2575fc;
            margin-bottom: 20px;
            text-align: center;
            font-size: 1.8rem;
        }
        
        .display {
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: right;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .operation {
            font-size: 1.2rem;
            color: #6c757d;
            min-height: 30px;
            word-break: break-all;
        }
        
        .result {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2575fc;
            word-break: break-all;
        }
        
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }
        
        button {
            border: none;
            padding: 18px 10px;
            font-size: 1.2rem;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-weight: 600;
        }
        
        .number {
            background: #f8f9fa;
            color: #333;
        }
        
        .number:hover {
            background: #e9ecef;
            transform: translateY(-2px);
        }
        
        .operator {
            background: #4dabf7;
            color: white;
        }
        
        .operator:hover {
            background: #339af0;
            transform: translateY(-2px);
        }
        
        .equals {
            background: #40c057;
            color: white;
        }
        
        .equals:hover {
            background: #2f9e44;
            transform: translateY(-2px);
        }
        
        .clear {
            background: #fa5252;
            color: white;
        }
        
        .clear:hover {
            background: #e03131;
            transform: translateY(-2px);
        }
        
        .zero {
            grid-column: span 2;
        }
        
        .features {
            flex: 1;
            min-width: 300px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .feature-box {
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .feature-box h3 {
            color: #2575fc;
            margin-bottom: 15px;
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .feature-box h3 i {
            color: #40c057;
        }
        
        .operations-list {
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .operations-list li {
            background: #e7f5ff;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: 500;
            color: #1971c2;
        }
        
        .history {
            max-height: 200px;
            overflow-y: auto;
            padding-right: 10px;
        }
        
        .history-item {
            padding: 10px;
            border-bottom: 1px solid #e9ecef;
            display: flex;
            justify-content: space-between;
        }
        
        .history-operation {
            color: #666;
        }
        
        .history-result {
            color: #2575fc;
            font-weight: bold;
        }
        
        .validation-box {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 15px;
            margin-top: 15px;
            color: #856404;
        }
        
        .alert {
            padding: 12px;
            border-radius: 8px;
            margin-top: 15px;
            display: none;
            font-weight: 500;
        }
        
        .alert-success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        
        .alert-error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        .api-section {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .api-input {
            padding: 12px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 1rem;
        }
        
        .api-buttons {
            display: flex;
            gap: 10px;
        }
        
        .api-btn {
            flex: 1;
            padding: 12px;
            background: #495057;
            color: white;
        }
        
        .api-btn:hover {
            background: #343a40;
        }
        
        @media (max-width: 768px) {
            .calculator-container {
                flex-direction: column;
            }
            
            .buttons {
                grid-template-columns: repeat(4, 1fr);
            }
            
            button {
                padding: 15px 5px;
                font-size: 1.1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-calculator"></i> Calculadora Flask</h1>
            <p>Sistema completo de calculadora con operaciones básicas y validaciones</p>
        </div>
        
        <div class="calculator-container">
            <div class="calculator">
                <h2>Calculadora Interactiva</h2>
                
                <div class="display">
                    <div class="operation" id="operation">0</div>
                    <div class="result" id="result">0</div>
                </div>
                
                <div class="buttons">
                    <button class="clear" onclick="clearDisplay()">C</button>
                    <button class="clear" onclick="deleteLast()">⌫</button>
                    <button class="operator" onclick="appendOperator('/')">/</button>
                    <button class="operator" onclick="appendOperator('*')">×</button>
                    
                    <button class="number" onclick="appendNumber('7')">7</button>
                    <button class="number" onclick="appendNumber('8')">8</button>
                    <button class="number" onclick="appendNumber('9')">9</button>
                    <button class="operator" onclick="appendOperator('-')">-</button>
                    
                    <button class="number" onclick="appendNumber('4')">4</button>
                    <button class="number" onclick="appendNumber('5')">5</button>
                    <button class="number" onclick="appendNumber('6')">6</button>
                    <button class="operator" onclick="appendOperator('+')">+</button>
                    
                    <button class="number" onclick="appendNumber('1')">1</button>
                    <button class="number" onclick="appendNumber('2')">2</button>
                    <button class="number" onclick="appendNumber('3')">3</button>
                    <button class="equals" onclick="calculate()" rowspan="2">=</button>
                    
                    <button class="number zero" onclick="appendNumber('0')">0</button>
                    <button class="number" onclick="appendDecimal()">.</button>
                </div>
                
                <div class="alert" id="alert"></div>
            </div>
            
            <div class="features">
                <!-- ===== PARTE 2: FEATURES INDIVIDUALES ===== -->
                <div class="feature-box">
                    <h3><i class="fas fa-plus-circle"></i> Suma y Resta</h3>
                    <p>Operaciones básicas de suma y resta con validación de entrada.</p>
                    <ul class="operations-list">
                        <li>5 + 3 = 8</li>
                        <li>10 - 4 = 6</li>
                        <li>-7 + 2 = -5</li>
                        <li>15 - 20 = -5</li>
                    </ul>
                    
                    <div class="api-section">
                        <h4>Prueba la API:</h4>
                        <input type="number" class="api-input" id="sumNum1" placeholder="Número 1">
                        <input type="number" class="api-input" id="sumNum2" placeholder="Número 2">
                        <div class="api-buttons">
                            <button class="api-btn" onclick="apiSum()">Sumar</button>
                            <button class="api-btn" onclick="apiSubtract()">Restar</button>
                        </div>
                    </div>
                </div>
                
                <!-- ===== PARTE 3: MULTIPLICACIÓN Y DIVISIÓN ===== -->
                <div class="feature-box">
                    <h3><i class="fas fa-times-circle"></i> Multiplicación y División</h3>
                    <p>Operaciones de multiplicación y división con manejo de errores.</p>
                    <ul class="operations-list">
                        <li>6 × 7 = 42</li>
                        <li>15 ÷ 3 = 5</li>
                        <li>8 × 0 = 0</li>
                        <li>10 ÷ 2 = 5</li>
                    </ul>
                    
                    <div class="validation-box">
                        <strong>Validación:</strong> La división por cero está bloqueada.
                    </div>
                    
                    <div class="api-section">
                        <h4>Prueba la API:</h4>
                        <input type="number" class="api-input" id="mulNum1" placeholder="Número 1">
                        <input type="number" class="api-input" id="mulNum2" placeholder="Número 2">
                        <div class="api-buttons">
                            <button class="api-btn" onclick="apiMultiply()">Multiplicar</button>
                            <button class="api-btn" onclick="apiDivide()">Dividir</button>
                        </div>
                    </div>
                </div>
                
                <!-- Historial de operaciones -->
                <div class="feature-box">
                    <h3><i class="fas fa-history"></i> Historial</h3>
                    <div class="history" id="history">
                        <!-- El historial se llenará dinámicamente -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // ===== PARTE 1: LÓGICA DE LA CALCULADORA (Frontend) =====
        let currentOperation = '0';
        let currentResult = '0';
        let operationHistory = [];
        
        function updateDisplay() {
            document.getElementById('operation').textContent = currentOperation;
            document.getElementById('result').textContent = currentResult;
        }
        
        function appendNumber(num) {
            if (currentOperation === '0' || currentOperation === 'Error') {
                currentOperation = num;
            } else {
                currentOperation += num;
            }
            updateDisplay();
        }
        
        function appendOperator(op) {
            if (currentOperation === 'Error') {
                currentOperation = '0';
            }
            
            const lastChar = currentOperation.slice(-1);
            if ('+-*/'.includes(lastChar)) {
                currentOperation = currentOperation.slice(0, -1) + op;
            } else {
                currentOperation += op;
            }
            updateDisplay();
        }
        
        function appendDecimal() {
            if (currentOperation === 'Error') {
                currentOperation = '0.';
            } else if (!currentOperation.includes('.')) {
                currentOperation += '.';
            }
            updateDisplay();
        }
        
        function clearDisplay() {
            currentOperation = '0';
            currentResult = '0';
            updateDisplay();
            hideAlert();
        }
        
        function deleteLast() {
            if (currentOperation.length > 1) {
                currentOperation = currentOperation.slice(0, -1);
            } else {
                currentOperation = '0';
            }
            updateDisplay();
        }
        
        function showAlert(message, type) {
            const alert = document.getElementById('alert');
            alert.textContent = message;
            alert.className = 'alert ' + type;
            alert.style.display = 'block';
        }
        
        function hideAlert() {
            document.getElementById('alert').style.display = 'none';
        }
        
        // ===== PARTE 2: LLAMADAS A LA API (Suma y Resta) =====
        async function apiSum() {
            const num1 = document.getElementById('sumNum1').value;
            const num2 = document.getElementById('sumNum2').value;
            
            if (!num1 || !num2) {
                showAlert('Por favor ingresa ambos números', 'alert-error');
                return;
            }
            
            try {
                const response = await fetch('/api/sumar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ num1: parseFloat(num1), num2: parseFloat(num2) })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showAlert(data.error, 'alert-error');
                } else {
                    showAlert(`Resultado: ${data.resultado}`, 'alert-success');
                    addToHistory(`${num1} + ${num2} = ${data.resultado}`);
                }
            } catch (error) {
                showAlert('Error de conexión: ' + error.message, 'alert-error');
            }
        }
        
        async function apiSubtract() {
            const num1 = document.getElementById('sumNum1').value;
            const num2 = document.getElementById('sumNum2').value;
            
            if (!num1 || !num2) {
                showAlert('Por favor ingresa ambos números', 'alert-error');
                return;
            }
            
            try {
                const response = await fetch('/api/restar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ num1: parseFloat(num1), num2: parseFloat(num2) })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showAlert(data.error, 'alert-error');
                } else {
                    showAlert(`Resultado: ${data.resultado}`, 'alert-success');
                    addToHistory(`${num1} - ${num2} = ${data.resultado}`);
                }
            } catch (error) {
                showAlert('Error de conexión: ' + error.message, 'alert-error');
            }
        }

        // ===== PARTE 3: LLAMADAS A LA API (Multiplicación y División) =====
        async function apiMultiply() {
            const num1 = document.getElementById('mulNum1').value;
            const num2 = document.getElementById('mulNum2').value;
            
            if (!num1 || !num2) {
                showAlert('Por favor ingresa ambos números', 'alert-error');
                return;
            }
            
            try {
                const response = await fetch('/api/multiplicar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ num1: parseFloat(num1), num2: parseFloat(num2) })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showAlert(data.error, 'alert-error');
                } else {
                    showAlert(`Resultado: ${data.resultado}`, 'alert-success');
                    addToHistory(`${num1} × ${num2} = ${data.resultado}`);
                }
            } catch (error) {
                showAlert('Error de conexión: ' + error.message, 'alert-error');
            }
        }
        
        async function apiDivide() {
            const num1 = document.getElementById('mulNum1').value;
            const num2 = document.getElementById('mulNum2').value;
            
            if (!num1 || !num2) {
                showAlert('Por favor ingresa ambos números', 'alert-error');
                return;
            }
            
            try {
                const response = await fetch('/api/dividir', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ num1: parseFloat(num1), num2: parseFloat(num2) })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showAlert(data.error, 'alert-error');
                } else {
                    showAlert(`Resultado: ${data.resultado}`, 'alert-success');
                    addToHistory(`${num1} ÷ ${num2} = ${data.resultado}`);
                }
            } catch (error) {
                showAlert('Error de conexión: ' + error.message, 'alert-error');
            }
        }
        
        // Función para calcular la operación actual
        async function calculate() {
            if (currentOperation === '0' || currentOperation === 'Error') {
                return;
            }
            
            // Validar que la operación termine con un número
            const lastChar = currentOperation.slice(-1);
            if ('+-*/'.includes(lastChar)) {
                showAlert('La operación no puede terminar con un operador', 'alert-error');
                return;
            }
            
            try {
                const response = await fetch('/api/calcular', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ operacion: currentOperation })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showAlert(data.error, 'alert-error');
                    currentResult = 'Error';
                } else {
                    currentResult = data.resultado;
                    addToHistory(`${currentOperation} = ${data.resultado}`);
                    showAlert('Cálculo exitoso', 'alert-success');
                }
            } catch (error) {
                showAlert('Error de conexión: ' + error.message, 'alert-error');
                currentResult = 'Error';
            }
            
            updateDisplay();
        }
        
        function addToHistory(operation) {
            operationHistory.unshift(operation);
            if (operationHistory.length > 5) {
                operationHistory.pop();
            }
            
            const historyElement = document.getElementById('history');
            historyElement.innerHTML = '';
            
            operationHistory.forEach(op => {
                const item = document.createElement('div');
                item.className = 'history-item';
                item.innerHTML = `
                    <span class="history-operation">${op.split('=')[0]}=</span>
                    <span class="history-result">${op.split('=')[1]}</span>
                `;
                historyElement.appendChild(item);
            });
        }
        
        // Inicializar
        updateDisplay();
    </script>
</body>
</html>
'''

# ===== PARTE 4: RUTAS FLASK (Backend) =====
@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

# ===== PARTE 1: SUMA Y RESTA =====
@app.route("/api/sumar", methods=['POST'])
def sumar():
    try:
        data = request.get_json()
        
        # Validaciones
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({'error': 'Datos incompletos'}), 400
            
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
        except ValueError:
            return jsonify({'error': 'Los valores deben ser números válidos'}), 400
        
        resultado = num1 + num2
        return jsonify({'resultado': resultado})
        
    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

@app.route("/api/restar", methods=['POST'])
def restar():
    try:
        data = request.get_json()
        
        # Validaciones
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({'error': 'Datos incompletos'}), 400
            
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
        except ValueError:
            return jsonify({'error': 'Los valores deben ser números válidos'}), 400
        
        resultado = num1 - num2
        return jsonify({'resultado': resultado})
        
    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

# ===== PARTE 2: MULTIPLICACIÓN Y DIVISIÓN =====
@app.route("/api/multiplicar", methods=['POST'])
def multiplicar():
    try:
        data = request.get_json()
        
        # Validaciones
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({'error': 'Datos incompletos'}), 400
            
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
        except ValueError:
            return jsonify({'error': 'Los valores deben ser números válidos'}), 400
        
        resultado = num1 * num2
        return jsonify({'resultado': resultado})
        
    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

@app.route("/api/dividir", methods=['POST'])
def dividir():
    try:
        data = request.get_json()
        
        # Validaciones
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({'error': 'Datos incompletos'}), 400
            
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
        except ValueError:
            return jsonify({'error': 'Los valores deben ser números válidos'}), 400
        
        # Validación especial: división por cero
        if num2 == 0:
            return jsonify({'error': 'No se puede dividir por cero'}), 400
        
        resultado = num1 / num2
        return jsonify({'resultado': round(resultado, 10)})  # Redondear para evitar decimales largos
        
    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

# ===== PARTE 3: CÁLCULO COMPLETO =====
@app.route("/api/calcular", methods=['POST'])
def calcular():
    try:
        data = request.get_json()
        
        # Validaciones
        if not data or 'operacion' not in data:
            return jsonify({'error': 'Operación no proporcionada'}), 400
            
        operacion = data['operacion']
        
        # Validar que la operación solo contenga caracteres permitidos
        import re
        if not re.match(r'^[\d+\-*/. ]+$', operacion):
            return jsonify({'error': 'Caracteres no permitidos en la operación'}), 400
        
        # Validar que no haya dos operadores consecutivos
        if re.search(r'[+\-*/]{2,}', operacion):
            return jsonify({'error': 'Operadores consecutivos no permitidos'}), 400
        
        # Reemplazar caracteres para evaluación segura
        operacion_eval = operacion.replace('×', '*').replace('÷', '/')
        
        try:
            # Usar eval con precaución (en producción usar una librería como ast.literal_eval)
            resultado = eval(operacion_eval)
            
            # Validar que el resultado sea un número
            if not isinstance(resultado, (int, float)):
                return jsonify({'error': 'Resultado no es un número válido'}), 400
                
            return jsonify({'resultado': round(resultado, 10)})
            
        except ZeroDivisionError:
            return jsonify({'error': 'División por cero no permitida'}), 400
        except SyntaxError:
            return jsonify({'error': 'Sintaxis de operación inválida'}), 400
        except Exception as e:
            return jsonify({'error': f'Error en el cálculo: {str(e)}'}), 400
            
    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)