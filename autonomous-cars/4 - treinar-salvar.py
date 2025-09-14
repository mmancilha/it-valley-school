import cv2
import joblib
import os

tamanho = 64
pasta_mulheres = "./modelos/mulher"
pasta_homem = "./modelos/homem"

imagens = []
rotulos = []