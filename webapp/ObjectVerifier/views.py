import os
import numpy as np
import joblib
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .forms import ImageUploadForm
from .models import UploadedImage
from PIL import Image
from django.conf import settings

# Load your models
pca = joblib.load(os.path.join(settings.BASE_DIR, 'ml_models', 'pca.pkl'))
svm = joblib.load(os.path.join(settings.BASE_DIR, 'ml_models', 'svm.pkl'))
knn = joblib.load(os.path.join(settings.BASE_DIR, 'ml_models', 'knn.pkl'))

def handle_uploaded_file(file_path):
    try:
        # Open and process the image
        image = Image.open(file_path)
        image = image.resize((750, 500))
        image_array = np.array(image).flatten()

        # Transform the image using PCA
        transformed_image = pca.transform([image_array])
        
        # Perform predictions
        svm_prediction = svm.predict(transformed_image)
        knn_prediction = knn.predict(transformed_image)

        return svm_prediction[0], knn_prediction[0]
    except Exception as e:
        print(f"Error processing file: {e}")
        return None, None

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            # Save the uploaded file
            fs = FileSystemStorage()
            file_path = fs.save(uploaded_image.image.name, uploaded_image.image)
            file_path = fs.path(file_path)

            # Perform predictions
            svm_pred, knn_pred = handle_uploaded_file(file_path)

            # Remove the file after prediction
            os.remove(file_path)

            if svm_pred is not None and knn_pred is not None:
                return redirect(f'/result/?svm_pred={svm_pred}&knn_pred={knn_pred}&image_url={uploaded_image.image.url}')
            else:
                return render(request, 'home.html', {'form': form, 'error': 'Error processing the image.'})
        else:
            return render(request, 'home.html', {'form': form, 'error': 'Invalid form submission.'})
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})

def result(request):    
    svm_pred = request.GET.get('svm_pred')
    knn_pred = request.GET.get('knn_pred')
    image_url = request.GET.get('image_url')
    context = {
        'svm_pred': svm_pred,
        'knn_pred': knn_pred,
        'image_url': image_url,
    }
    return render(request, 'result.html', context)
