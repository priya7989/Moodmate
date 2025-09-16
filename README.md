# MoodMate: Emotion Detection & Music Recommendation System

## Project Objective
MoodMate is an intelligent system designed to detect a user's emotional state from facial images or text input and recommend music that aligns with or enhances the user's mood using AI/ML techniques. The project aims to integrate computer vision and natural language processing with recommendation systems to create a mood-aware music suggestion platform.

## Key Outcomes
- Develop expertise in emotion detection from facial images and text.
- Build a music recommendation engine mapped to detected emotions.
- Deliver an interactive prototype offering real-time emotion-based music suggestions.

## Datasets Used
- **FER-2013 Dataset**: Used for facial emotion detection via CNN model.
- **Music Dataset**: Subsets from Million Song Dataset or Last.fm for music metadata including tags, genres, mood.

## Modules Implemented
1. **Data Collection & Preprocessing**  
   - Clean and preprocess image and text emotion datasets.
   - Extract features from music datasets for emotion-tag mapping.

2. **Emotion Detection Module**  
   - Text-based emotion detection using BERT transformer model.
   - Image-based emotion detection using CNN trained on FER-2013.

3. **Music Recommendation Engine**  
   - Map detected emotions to relevant music tags like happy, sad, calm.
   - Create a content-based filtering recommendation system.

4. **User Interface**  
   - Web or desktop UI allowing image upload or text input.
   - Real-time display of detected emotions and suggested playlists.

5. **Evaluation & Integration**  
   - Test models for accuracy and usability.
   - Integrate modules for smooth data flow and response.

## BERT Text Emotion Classifier
- Detects emotions such as joy, sadness, anger, fear, surprise, love, and trust.
- Uses Hugging Face transformers library with PyTorch backend.
- Outputs predicted emotion label with confidence scores.


