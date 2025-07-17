# Web-User Identification Using Sequential Web Page Visits

This project focuses on identifying whether a sequence of visited web pages belongs to a specific user (Alice) or not. The problem lies at the intersection of sequential pattern mining and behavioral psychology, and uses real-world proxy server data collected from Blaise Pascal University.

## 🧠 Project Overview

The goal is to develop a classification algorithm that can determine whether a session (a sequential list of web pages visited by a user) belongs to **Alice** or **someone else**.

This task was inspired by the paper:
> *"A Tool for Classification of Sequential Data"*  
> by Giacomo Kahn, Yannick Loiseau, and Olivier Raynaud.

## 📊 Dataset

The dataset was gathered from the proxy servers of Blaise Pascal University. Each session represents a chronological sequence of web pages accessed by a single user.

- **Format**: Each line/session contains a sequence of web pages.
- **Labels**: Each session is labeled either as belonging to **Alice** or **Other**.
 
