# Handwriting Digit Recognition Project

[![Project Demo](https://example.com/day1_video_thumbnail.png)](1/Day1.mp4)
[![Project Demo](https://example.com/day2_video_thumbnail.png)](1/Day2.mp4)
[![Project Demo](https://example.com/day3_video_thumbnail.png)](1/Day3.mp4)
[![Project Demo](https://example.com/day4_video_thumbnail.png)](1/Day4.mp4)

This repository contains my progress on the Handwriting Digit Recognition project for the #100days25projectchallenge. Each day, I documented my updates and achievements.

## Table of Contents

- [Day 1 Update](#day-1-update)
- [Day 2 Update](#day-2-update)
- [Day 3 Update](#day-3-update)
- [Day 4 Update](#day-4-update)
- [Project Details](#project-details)

## Day 1 Update

🚀 Project 1 Day 1 Update! 📝

Excited to share my progress on Handwriting Digit Recognition for the #100days25projectchallenge! 🤩 Today, I focused on generating my own dataset and exploring data augmentation techniques. I started by creating digit images using Paint and captured them using pyscreenshot. It was a fun process! 😄

To enrich my dataset, I applied data augmentation techniques, transforming just 5 images per digit into 500 unique images. This involved techniques like rotation, scaling, and translation. It was challenging, but I persisted and successfully generated a diverse dataset!

I organized my dataset into two sets: `df_original` containing the original digit images, and `df_ag` containing the augmented images. This division will help me compare the performance of my models later on.

In addition, I'm planning to take this project a step further by creating a simple GUI to enhance the user experience and showcase the digit recognition capabilities.

Overall, it was an engaging day spent on image generation, augmentation, and preparing for the next steps. I invested around 3 hours to understand and implement the techniques effectively. 💡

Stay tuned for tomorrow's update! I'll be diving into preprocessing and exploring different machine learning algorithms for digit recognition. Let's keep the momentum going! 💪🔥

Check out my progress on [GitHub](https://example.com/day1_github).

[Watch Day 1 Video](https://example.com/day1_video)

## Day 2 Update

🚀 Project 1 Day 2 Update! 📝

Today, I made significant progress in preprocessing the dataset for my Handwriting Digit Recognition project as part of the #100days25projectchallenge.

I began by thoroughly examining the dataset, checking for null values, and splitting it into features and labels. To ensure accuracy, I handled the original and augmented data separately, organizing them meticulously for further analysis.

In order to gain deeper insights into the dataset, I utilized the power of matplotlib to visually explore both the original and augmented images. This allowed me to unravel the intricate variations present in the digit samples and develop a comprehensive understanding of the data.

Moving forward, I trained a total of 14 models using the preprocessed data, employing diverse algorithms such as SVC, RFC, GradientBoosting, NaiveBayes, and KNN with various parameters. After rigorous evaluation, the KNN model with 1 neighbor emerged as the clear frontrunner, showcasing exceptional performance. The original dataset achieved an accuracy of 60%, while the augmented dataset displayed an impressive accuracy of 93%. This stark contrast was expected, considering the limited size of the original dataset for training.

Looking ahead to tomorrow, my focus will shift towards creating a simplified and intuitive GUI for the project. By harnessing the capabilities of different libraries, I aim to develop an engaging user interface that seamlessly demonstrates the remarkable digit recognition capabilities of my project.

Stay tuned for tomorrow's update as I delve deeper into GUI development, aiming to enhance the project's accessibility and visual appeal. Let's maintain the unwavering momentum! 💪🔥

Check out my progress on [GitHub](https://example.com/day2_github).

[Watch Day 2 Video](https://example.com/day2_video)

## Day 3 Update

🚀 Project 1 Day 3 Update! 📝

Today, despite a slow start, I made progress in my Handwriting Digit Recognition project for the #100days25projectchallenge. In just 1.5 hours, I accomplished three crucial tasks that set the foundation for tomorrow's work.

Firstly, I summarized the project's tables, organizing columns with classification real names, accuracy, and model names. This summary provides a clear overview of different models' performance and their corresponding accuracies.

Next, I explored real-time demo prediction using a paint application. I implemented a feature that allows me to draw digits in real-time and witness the model's predictions with a 5-second delay. It's an exciting experience to see the system in action!

Additionally, I took the necessary step of converting a few problematic cells into RawNB format. These cells were overwriting my images whenever I restarted the kernel. This modification will help preserve the images and prevent any unintended data loss.

Lastly, I researched various GUI-making libraries and found tkinter to be a versatile and user-friendly option. Tomorrow, I plan to utilize tkinter to develop an impressive GUI for my project.

However, I encountered a challenge with occasional misclassifications. The model sometimes mistakes the digit 2 for 5, 4 for 9, and 3 for 5. This impacts the accuracy of the system.

To address this issue, I have two options. One is to proceed with the GUI interface, accepting occasional incorrect predictions. The other is to implement deep learning techniques to improve the model's performance. Alternatively, hyperparameter tuning is another possibility, though I'm less familiar with its code implementation.

I will carefully consider these options and make a decision tomorrow. Stay tuned for the next update as I work towards enhancing the project further!

Check out my progress on [GitHub](https://example.com/day3_github).

[Watch Day 3 Video](https://example.com/day3_video)

## Day 4 Update

🚀 Project 1 Day 4 Update! 📝

On the fourth and final day of my Handwriting Digit Recognition project for the #100days25projectchallenge, I dedicated roughly two hours to building a deep learning model using convolutional neural networks (CNN).

I began by splitting the dataset into new x_train and y_train, using only augmented images. I trained the model, fit the values in it, and ran it for 10 epochs. The accuracy was around 70%, so I increased the number of epochs, leading to an impressive accuracy of 95%.

To ensure ease of access and organization, I created separate files for data and for running the GUI for machine learning models and the GUI for CNN separately.

Although I am not entirely satisfied with the GUI's current state, I plan to upgrade it in the future. As my exams are approaching, I consider this project complete. In total, I spent 3+3+1.5+2=9.5 hours on this project over the course of four days.

Tomorrow, I am starting a new project on coloring black and white images, and I am excited to see what I can achieve. Thank you for following my progress on this project, and stay tuned for updates on my future projects!

Check out my progress on [GitHub](https://example.com/day4_github).

[Watch Day 4 Video](https://example.com/day4_video)

## Project Details

- **Date:** 11-05-23
- **Challenge:** #100days25projectchallenge
- **Tags:** machinelearning, digitrecognition, datageneration, augmentationtechniques, GUIdevelopment, project

Feel free to explore my progress on GitHub and watch the accompanying videos for each day's updates!

