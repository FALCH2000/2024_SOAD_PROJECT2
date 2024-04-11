# 2024_SOAD_PROJECT2

Proyecto 2 del curso de SOA del año 2024.

### Hacer deploy de cloud function:

```
gcloud functions deploy meal_recommendation --gen2 --runtime=python312 --region=us-west1 --source=. --entry-point=get_recommendation --trigger-http --allow-unauthenticated
```
