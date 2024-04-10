## Como ejecutar
Se debe correr el siguiente comando en consola:
- source env/bin/activate
Además, instale los requerimientos con:
- pip install -r requirements.txt

## Como desplegar manualmente
Ejecutar el siguiente comando:
    gcloud functions deploy reservacion --gen2 --runtime=python312 --region=us-west1 --source=.     --entry-point=gestionar_reservacion --trigger-http --allow-unauthenticated
