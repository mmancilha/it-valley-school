import cv2
import joblib

print('Carregando modelo...')
modelo = joblib.load('modelos/modelo.joblib')
print('Modelo carregado com sucesso!')