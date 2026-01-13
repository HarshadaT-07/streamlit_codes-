import google.generativeai as genai

genai.configure(api_key="AIzaSyAhZFfWzRppbsqmPc1OQqO6Ew7hQ_CxpqI")

for model in genai.list_models():
    print(model.name)
