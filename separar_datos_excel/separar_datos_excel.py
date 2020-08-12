import pandas as pd
#pip install pandas
#pip install xlrd
#pip install openpyxl

path_archivo_excel = 'entrenamiento.xlsx'

datos = pd.read_excel(path_archivo_excel)
#print(datos)

datos_separados = datos['Estatus'].unique()
#print(datos_separados)

for dato in datos_separados:
    nuevos_datos = datos[datos['Estatus'] == dato]
    nuevo_doc_excel = "entrenamiento_" + dato + ".xlsx"
    nuevos_datos.to_excel(nuevo_doc_excel, index = False)

print("Script Ejecutado Correctamente!")