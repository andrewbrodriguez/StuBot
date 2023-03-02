# StuBot
Chat Bot for the Student Center, Using this Repo to Dump Unity to School Machine


## Vision component
All the vision stuff is in the vision directory. 

Setup: 
```
cd vision
conda create env -f environment.yml
conda activate stubot
python face_recog.py --emotion
```

When you run deepface, models will be downloaded automatically. 