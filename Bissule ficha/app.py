import tkinter as tk
from tkinter import ttk
import sqlite3
from openpyxl import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

conn = sqlite3.connect('exercicios.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS exercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

exercicios = [
    'Supino', 'Agachamento', 'Rosca Direta', 'Desenvolvimento de Ombros', 'Leg Press', 
    'Extensão de Pernas', 'Flexão de Pernas', 'Puxada Frontal', 'Remada Curvada', 'Elevação Lateral',
    'Crucifixo', 'Tríceps Corda', 'Tríceps Testa', 'Rosca Scott', 'Rosca Martelo', 
    'Abdominal Supra', 'Abdominal Infra', 'Abdominal Oblíquo', 'Prancha', 'Flexão de Braços',
    'Afundo', 'Cadeira Adutora', 'Cadeira Abdutora', 'Glúteo 4 Apoios', 'Glúteo Máquina',
    'Levantamento Terra', 'Stiff', 'Remada Cavalinho', 'Remada Unilateral', 'Puxada Aberta',
    'Puxada Triângulo', 'Desenvolvimento Arnold', 'Encolhimento de Ombros', 'Rosca Concentrada', 
    'Rosca Inversa', 'Tríceps Pulley', 'Tríceps Francês', 'Elevação Frontal', 'Remada Alta', 
    'Kickback', 'Voador Peitoral', 'Voador Inverso', 'Pull Over', 'Extensão de Quadril', 
    'Abdução de Quadril', 'Addução de Quadril', 'Panturrilha em Pé', 'Panturrilha Sentado',
    'Box Jump', 'Burpee', 'Kettlebell Swing', 'Mountain Climbers', 'Pular Corda',
    'Sprints', 'Corrida', 'Bicicleta Ergométrica', 'Elíptico', 'Remo Ergométrico',
    'Flexão Diamante', 'Flexão Decline', 'Flexão Incline', 'Clean and Press', 'Snatch',
    'Clean', 'Jerk', 'Wall Ball', 'Salto no Caixote', 'Agachamento Búlgaro',
    'Caminhada', 'Corrida Estacionária', 'Swing com Haltere', 'Tire Flip', 'Battle Rope',
    'Farmers Walk', 'Renegade Row', 'Plancha com Elevação de Braço', 'Superman', 'Ponte',
    'Dips', 'Pistols', 'Lunges', 'Pull-Ups', 'Chin-Ups',
    'Hammer Curl', 'Cable Cross Over', 'Face Pull', 'Incline Bench Press', 'Decline Bench Press',
    'Overhead Press', 'Arnold Press', 'Lateral Raise', 'Front Raise', 'Rear Delt Fly',
    'Shrugs', 'Seated Row', 'T-Bar Row', 'Lat Pulldown', 'Reverse Grip Pulldown',
    'Cable Row', 'Inverted Row', 'Single Arm Row', 'Deadlift', 'Sumo Deadlift',
    'Hex Bar Deadlift', 'Romanian Deadlift', 'Good Mornings', 'Hip Thrust', 'Cable Kickbacks',
    'Fire Hydrants', 'Seated Calf Raise', 'Standing Calf Raise', 'Calf Press', 'Toe Raises'
]

for exercicio in exercicios:
    cursor.execute("INSERT INTO exercicios (nome) VALUES (?)", (exercicio,))

conn.commit()
conn.close()

def fetch_exercises():
    conn = sqlite3.connect('exercicios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exercicios")
    rows = cursor.fetchall()
    conn.close()
    return rows

def generate_excel(trainer_name, client_name, selected_exercises):
    wb = Workbook()
    ws = wb.active
    ws.append(["Nome do Treinador", trainer_name])
    ws.append(["Nome do Cliente", client_name])
    ws.append([])
    ws.append(["Nome do Exercício", "Tipo de Treino", "Repetições", "Séries", "Peso", "Obs"])
    for exercise in selected_exercises:
        ws.append(exercise)
    wb.save("Ficha_de_Exercicios.xlsx")

def generate_pdf(trainer_name, client_name, selected_exercises):
    doc = SimpleDocTemplate("Ficha_de_Exercicios.pdf", pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    styleH = styles['Heading1']
    styleN = styles['Normal']
    elements.append(Paragraph("Ficha de Exercícios", styleH))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Nome do Treinador: {trainer_name}", styleN))
    elements.append(Paragraph(f"Nome do Cliente: {client_name}", styleN))
    elements.append(Spacer(1, 12))
    data = [["Tipo Treino", "Nome do Exercício", "Repetições", "Séries", "Peso", "Obs"]] + selected_exercises
    table = Table(data, colWidths=[1 * inch, 2 * inch, inch, inch, inch, 1.5 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPACEAFTER', (0, 0), (-1, -1), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))
    doc.build(elements)

def add_exercise():
    selected_exercise = exercise_combobox.get()
    quantity = quantity_entry.get()
    sets = sets_entry.get()
    exercise_type = type_combobox.get()
    weight = weight_entry.get()
    obs = obs_entry.get()
    if selected_exercise and quantity and sets and exercise_type and weight:
        tree.insert("", tk.END, values=(exercise_type, selected_exercise, quantity, sets, weight, obs))

def delete_exercise():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

def on_generate():
    trainer_name = trainer_entry.get()
    client_name = client_entry.get()
    selected_exercises = [(tree.item(item, "values")) for item in tree.get_children()]
    generate_excel(trainer_name, client_name, selected_exercises)
    generate_pdf(trainer_name, client_name, selected_exercises)

def add_new_exercise():
    new_exercise = new_exercise_entry.get()
    if new_exercise:
        conn = sqlite3.connect('exercicios.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exercicios WHERE nome = ?", (new_exercise,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO exercicios (nome) VALUES(?)", (new_exercise,))
            conn.commit()
            exercise_combobox['values'] = [row[1] for row in fetch_exercises()]
        conn.close()

root = tk.Tk()
root.title("Gerador de Ficha de Exercícios")
root.geometry("700x850")
root.configure(bg='#f0f0f0')

style = ttk.Style()
style.configure("TLabel", font=('Arial', 12), background='#f0f0f0')
style.configure("TButton", font=('Arial', 12))
style.configure("TCombobox", font=('Arial', 12))

top_frame = tk.Frame(root, bg='#f0f0f0', bd=2, relief='solid')
top_frame.pack(pady=10, padx=10, fill='x')

trainer_label = ttk.Label(top_frame, text="Nome do Treinador:")
trainer_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
trainer_entry = ttk.Entry(top_frame, font=('Arial', 12))
trainer_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

client_label = ttk.Label(top_frame, text="Nome do Cliente:")
client_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
client_entry = ttk.Entry(top_frame, font=('Arial', 12))
client_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

middle_frame = tk.Frame(root, bg='#f0f0f0', bd=2, relief='solid')
middle_frame.pack(pady=10, padx=10, fill='both', expand=True)

new_exercise_entry = ttk.Entry(middle_frame, font=('Arial', 12))
new_exercise_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
new_exercise_button = ttk.Button(middle_frame, text="Adicionar Novo Exercício", command=add_new_exercise)
new_exercise_button.grid(row=0, column=2, padx=5, pady=5, sticky='w')

type_label = ttk.Label(middle_frame, text="Tipo de Treino:")
type_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
type_combobox = ttk.Combobox(middle_frame, values=["A", "B", "C", "D","E", "F"], font=('Arial', 12))
type_combobox.grid(row=1, column=1, padx=5, pady=5, sticky='w')

exercise_label = ttk.Label(middle_frame, text="Exercício:")
exercise_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
exercise_combobox = ttk.Combobox(middle_frame, values=[row[1] for row in fetch_exercises()], font=('Arial', 12))
exercise_combobox.grid(row=2, column=1, padx=5, pady=5, sticky='w')

quantity_label = ttk.Label(middle_frame, text="Repetições:")
quantity_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
quantity_entry = ttk.Entry(middle_frame, font=('Arial', 12))
quantity_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

sets_label = ttk.Label(middle_frame, text="Séries:")
sets_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
sets_entry = ttk.Entry(middle_frame, font=('Arial', 12))
sets_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

weight_label = ttk.Label(middle_frame, text="Peso:")
weight_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
weight_entry = ttk.Entry(middle_frame, font=('Arial', 12))
weight_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w')

obs_label = ttk.Label(middle_frame, text="Observações:")
obs_label.grid(row=6, column=0, padx=5, pady=5, sticky='e')
obs_entry = ttk.Entry(middle_frame, font=('Arial', 12))
obs_entry.grid(row=6, column=1, padx=5, pady=5, sticky='w')

add_button = ttk.Button(middle_frame, text="Adicionar Exercício", command=add_exercise)
add_button.grid(row=7, column=0, padx=5, pady=5, sticky='e')

delete_button = ttk.Button(middle_frame, text="Remover Exercício", command=delete_exercise)
delete_button.grid(row=7, column=1, padx=5, pady=5, sticky='w')

tree_frame = tk.Frame(root, bg='#f0f0f0', bd=2, relief='solid')
tree_frame.pack(pady=10, padx=10, fill='both', expand=True)

columns = ("Tipo Treino", "Exercício", "Repetições", "Séries", "Peso", "Obs")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center')
tree.pack(fill='both', expand=True)

bottom_frame = tk.Frame(root, bg='#f0f0f0', bd=2, relief='solid')
bottom_frame.pack(pady=10, padx=10, fill='x')

generate_button = ttk.Button(bottom_frame, text="Gerar Ficha", command=on_generate)
generate_button.pack(pady=10)

root.mainloop()
